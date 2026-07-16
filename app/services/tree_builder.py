from app.models.parser_node import Node


class TreeBuilder:

    def build(self, nodes):

        stack = []

        for node in nodes:

            while stack and stack[-1].level >= node.level:
                stack.pop()

            if stack:
                node.parent = stack[-1]
                stack[-1].children.append(node)

            stack.append(node)

        return nodes