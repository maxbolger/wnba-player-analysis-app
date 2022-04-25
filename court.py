import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

def draw_court(ax=None, color='black', lw=2, outer_lines=False, end_year=2013):
    """
    Draws a WNBA basketball court using matplotlib.

            Parameters:
                ax (matplotlib.axes): matplotlib axes for court to be drawn to
                color (str): The color to draw the lines of the court
                lw (int): The line width of the lines of the court
                outer_lines (bool): Whether or not the outer lines should be drawn

            Returns:
                ax (matplotlib.axes): A matplotlib axes of the court
    """
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    ### Create the basketball hoop ###
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    ### Create backboard ###
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    ### The paint ###
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)
    # Create free throw top arc
    if end_year <= 2003:
        top_free_throw = Arc((0, 142.5), 120, 110, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    else:
        top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)

    ### Three point line ###
    if end_year >= 2013:
        # Create the side 3pt lines
        corner_three_a = Rectangle((-220, -47.5), 0, 75.5, linewidth=lw, color=color)
        corner_three_b = Rectangle((220, -47.5), 0, 75.5, linewidth=lw, color=color)
        # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
        three_arc = Arc((0, 0), 443.6, 443, theta1=7, theta2=173, linewidth=lw, color=color)
    elif end_year <= 2003:
        corner_three_a = Rectangle((-197, -47.5), 0, 75.5, linewidth=lw, color=color)
        corner_three_b = Rectangle((197, -47.5), 0, 75.5, linewidth=lw, color=color)
        three_arc = Arc((0, 0), 397.75, 394, theta1=7, theta2=173, linewidth=lw, color=color)
    else:
        corner_three_a = Rectangle((-205, -47.5), 0, 75.5, linewidth=lw, color=color)
        corner_three_b = Rectangle((205, -47.5), 0, 75.5, linewidth=lw, color=color)
        three_arc = Arc((0, 0), 414, 410, theta1=7, theta2=173, linewidth=lw, color=color)

    ### Center Court ###
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax
