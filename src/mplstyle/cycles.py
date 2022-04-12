from cycler import cycler 
from mplstyle import defaults
# List of plotting line styles
# cycler 1: line style series
# cycler 2: line color series
# cycler 3: line width series
# cycler 4: marker style series
# cycler 5: marker size series
# cycler 6: marker face color series
# cycler 7: marker edge color series
# cycler 8: marker edge width series
# cycler 9: alpha value series

def series_linestyle():
    return cycler(linestyle=list(defaults.line_styles.values()))

def series_linewidth():
    return cycler(linewidth=list(defaults.line_widths.values()))

def series_color():
    return cycler(color=list(defaults.colors.values()))

def series_marker():
    return cycler(marker=list(defaults.markers.values()))

def series_markersize():
    return cycler(markersize=list(defaults.marker_sizes.values()))

def series_linestyle_color():
    colors = list(defaults.colors.values())
    linestyles=list(defaults.line_styles.values())
    upper_limit = len(colors) if len(colors) < len(linestyles) else len(linestyles)
    c1 = cycler(color=colors[:upper_limit])
    c2 = cycler(linestyle=linestyles[:upper_limit])
    return (c1+c2)

def series_marker_color():
    colors = list(defaults.colors.values())
    markers=list(defaults.markers.values())
    upper_limit = len(colors) if len(colors) < len(markers) else len(markers)
    c1 = cycler(color=colors[:upper_limit])
    c2 = cycler(marker=markers[:upper_limit])
    return (c1+c2)

def series_linestyle_marker_color():
    colors = list(defaults.colors.values())
    linestyles=list(defaults.line_styles.values())
    markers=list(defaults.markers.values())
    upper_limit = len(colors) if len(colors) < len(linestyles) else len(linestyles)
    upper_limit = upper_limit if upper_limit < len(markers) else len(markers)
    c1 = cycler(color=colors[:upper_limit])
    c2 = cycler(linestyle=linestyles[:upper_limit])
    c3 = cycler(marker=markers[:upper_limit])
    return (c1+c2+c3)