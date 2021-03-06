from zmodulo.plot.line.start_point import StartPoint
from zmodulo.plot.properties.condition import Condition
from zmodulo.plot.line.line_style import LineStyle


class PlotLine:
    """ The Z-tree PlotLine Template
    """

    def __init__(self, start_point, end_point,
                 line_style=None, condition=None, element_id=""):
        """
        :param start_point: plot line left coordinate
        :type start_point: StartPoint
        :param end_point: plot line right coordinate
        :type end_point: EndPoint
        :param line_style: line style
        :type line_style: Line
        :param condition: z-tree condition string
        :type condition: str
        :param element_id: z-tree plot entity ID
        :type element_id: str
        """
        self.start_point = start_point
        self.end_point = end_point

        if line_style is None:
            self.line = LineStyle()
        else:
            self.line = line_style

        if condition is None:
            self.condition = Condition()
        else:
            self.condition = condition

        self.element_id = element_id

        self.template = 'plotline "{id}"{{\n{body}}}'

    def to_str(self):
        """
        :return: z-tree plot entity string
        :rtype: str
        """
        text_id = self.element_id
        condition = self.condition.to_str()
        start_point = self.start_point.to_str()
        end_point = self.end_point.to_str()
        line_style = self.line.to_str()

        return self.template.format(id=text_id, body=condition + start_point + end_point + line_style)

