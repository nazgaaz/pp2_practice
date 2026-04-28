# TSIS 2 Paint Application — Extended Drawing Tools

In this project, I extended the Paint application by adding new drawing tools and improving the functionality using only Pygame built-in features.

First, I implemented the Pencil Tool for freehand drawing. The user can hold the left mouse button and draw continuously on the canvas. This was implemented using `pygame.draw.line()` between the previous and current mouse positions to create smooth drawing.

Second, I added the Straight Line Tool with live preview. The user clicks to set the start point, drags the mouse, and releases it to draw the final line. During dragging, the program creates a temporary copy of the canvas and shows a preview of the line before final rendering.

Third, I implemented three brush size levels:
- Small (2 px)
- Medium (5 px)
- Large (10 px)

The user can switch between brush sizes using keyboard keys `1`, `2`, and `3`.

The active brush size is applied to all drawing tools and shapes, including:
- pencil
- eraser
- line
- rectangle
- circle
- square
- right triangle
- equilateral triangle
- rhombus

I also implemented the Flood-Fill Tool. When the user clicks inside a closed region, the selected area is filled with the current color. This feature uses `surface.get_at()` to read pixel colors and `surface.set_at()` to update them. A queue-based algorithm is used to fill neighboring pixels with the same color.

Another feature added is the Text Tool. The user clicks on the canvas to place a text cursor, types characters in real time, presses `Enter` to confirm and render the text permanently, or presses `Escape` to cancel text input.

I added the Save Canvas function using `Ctrl + S`. The current canvas is saved as a `.png` image file using `pygame.image.save()`. The filename includes the current date and time using Python’s `datetime` module, so files do not overwrite each other.

I implemented all required geometric shapes:
- rectangle
- circle
- square
- right triangle
- equilateral triangle
- rhombus

The project structure was organized into separate files:

TSIS2/
├── paint.py
├── tools.py

`paint.py` contains the main program logic, event handling, toolbar, and canvas rendering.  
`tools.py` contains helper functions for drawing shapes and performing flood-fill.

This project fully meets all assignment requirements: pencil tool, line tool with live preview, three brush sizes, flood-fill, save canvas, text tool, all required shapes, and clear project structure.
