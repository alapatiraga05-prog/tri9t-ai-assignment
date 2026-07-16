class Node:

    def __init__(self, heading, level):
        self.heading = heading
        self.level = level
        self.body = ""

        self.parent = None
        self.children = []

    def __repr__(self):
        return self.heading