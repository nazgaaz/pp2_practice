import re
import json
from pathlib import Path
from typing import Dict, Any, List, Optional


RAW_PATH = Path(__file__).with_name("raw.txt")


def to_number(s: str) -> float:
    """
    Converts "18 009,00" or "1 200,00" -> 18009.00 / 1200.00
    Also removes any whitespace like '\n' and '\t'.
    """
    s = re.sub(r"\s+", "", s)     # ✅ убираем ВСЕ пробелы/переносы/табуляции
    s = s.replace("\u00a0", "")   # на всякий случай неразрывный пробел
    s = s.replace(",", ".")       # запятая -> точка
    return float(s)


def parse_datetime(text: str) -> Optional[str]:
    # Время: 18.04.2019 11:13:58
    m = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
    if not m:
        return None
    return f"{m.group(1)} {m.group(2)}"


def parse_payment_method(text: str) -> Optional[str]:
    # В чеке есть "Банковская карта:"
    if re.search(r"\bБанковская\s+карта\b", text, re.IGNORECASE):
        return "bank_card"
    # можно расширить под "Наличные", "Kaspi", "QR" и т.д.
    if re.search(r"\bНаличные\b", text, re.IGNORECASE):
        return "cash"
    return None


def parse_total(text: str) -> Optional[float]:
    # ИТОГО:
    # 18 009,00
    m = re.search(r"ИТОГО:\s*\n\s*([\d\s]+,\d{2})", text)
    if not m:
        return None
    return to_number(m.group(1))


def parse_items(lines: List[str]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []

    qty_price_re = re.compile(r"^\s*(\d+,\d{3})\s*x\s*([\d\s]+,\d{2})\s*$")
    money_re = re.compile(r"^\s*([\d\s]+,\d{2})\s*$")

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Номер позиции: "1." "2." ...
        if re.match(r"^\d+\.$", line):
            # Название товара
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i >= len(lines):
                break

            name = lines[i].strip()

            # Строка qty x price
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i >= len(lines):
                break

            m_qp = qty_price_re.match(lines[i].strip())
            if not m_qp:
                continue

            qty = to_number(m_qp.group(1))
            unit_price = to_number(m_qp.group(2))

            # Сумма позиции
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i >= len(lines):
                break

            m_sum = money_re.match(lines[i].strip())
            if not m_sum:
                continue

            line_total = to_number(m_sum.group(1))

            items.append({
                "name": name,
                "quantity": qty,
                "unit_price": unit_price,
                "line_total": line_total
            })

        i += 1

    return items


def extract_all_prices(text: str) -> List[float]:
    """
    Extracts all prices like:
    1200,00 or 1 200,00 or 1200.00 or 1 200.00

    ✅ IMPORTANT: we allow only normal spaces, NOT '\s',
    because '\s' includes '\n' and it caused '150\\n1.00'
    """
    raw = re.findall(r"(\d[\d ]*[,.]\d{2})", text)  # ✅ only digits + normal spaces
    return [to_number(x) for x in raw]


def main() -> None:
    text = RAW_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    items = parse_items(lines)
    total = parse_total(text)
    dt = parse_datetime(text)
    payment = parse_payment_method(text)

    computed_total = round(sum(it["line_total"] for it in items), 2) if items else None

    result: Dict[str, Any] = {
        "datetime": dt,
        "payment_method": payment,
        "total": total,
        "computed_total_from_items": computed_total,
        "items": items,
        "all_prices_found": extract_all_prices(text),
        "currency": "KZT"
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()