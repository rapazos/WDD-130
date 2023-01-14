from draw2d import \
   # start_drawing, draw_line, draw_oval, draw_arc, \
   # draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)

    draw_rectangle(canvas, 150, 200, 200, 250, outline="white", fill= "white") 

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
# from draw2d import \
#     start_drawing, draw_line, draw_oval, draw_arc, \
#     draw_rectangle, draw_polygon, draw_text, finish_drawing         


# def main():
#     # Width and height of the scene in pixels
#     scene_width = 800
#     scene_height = 500

#     # Call the start_drawing function in the draw2d.py library
#     # which will open a window and create a canvas.
#     canvas = start_drawing("Scene", scene_width, scene_height)

# # Call your drawing functions such
#     # as draw_sky and draw_ground here.
#     draw_pine_tree(canvas, 200, 150, 300, )
#     draw_grid(canvas, scene_width, scene_height, 50)

#     # Call the finish_drawing function
#     # in the draw2d.py library.
#     finish_drawing(canvas)


#  # Define your functions such as
#     # draw_sky and draw_ground here.
#     def draw_pine_tree(canvas, center_x, bottom, height):
#         #draw the trunk of the tree._
#         tunk_width = height / 10
#         trunk_height = height /8
#         left_t = height / trunk = center_x - trunk_width / 2
#         bottom_trunk = bottom
#         rightI_trunk = center_x + trunk_width / 2
#         trunk_top = bottom + trunk height
#         draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="brown")

#         # Draw the skirt of tree
#         skirt_width = height / 2
#         skirt_left = center_x - skirt_width / 2 
#         skirt_bottom = trunk_top
#         skirt_center = center_x
#         skirt_top = bottom + height
#         skirt_right = center_x + skirt_width / 2
#         draw_polygon(canvas,)



#     draw_sky(canvas, scene_width, scene_height)
#     draw_ground(canvas, scene_width, scene_height)


#     # Call the finish_drawing function
#     # in the draw2d.py library.
#     finish_drawing(canvas)

# # Call the main function so that
# # this program will start executing.
# main()