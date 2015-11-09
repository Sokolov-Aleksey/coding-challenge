# example of program that calculates the average degree of hashtags
from collections import defaultdict
import itertools


class HashGraph(object):
    def __init__(self):
        # list of tags-timestamp pairs, arranged by time
        self.timeline = []
        # keeps all edges from last 60 seconds
        self.edges = defaultdict(int)
        # keeps all distinct vertices from last 60 seconds
        self.vertices = defaultdict(int)

    def get_avg_degree(self):
        num_vertices = len(self.vertices)
        if num_vertices == 0:
            return 0.0
        # We have to multiply edges by 2 as we store each edge only once.
        return len(self.edges) * 2 / float(num_vertices)

    def process_tweet(self, tags, ts):
        # process edges if any
        if len(tags) > 1:
            # add tags to the timeline and edges to the pseudo-graph
            self.timeline.append((tags, ts))
            self._add_edges(tags)

        # treat all deprecated tweets
        for i, v in enumerate(self.timeline):
            tags, cur_time = v
            if ts - cur_time > 60:
                self._remove_edges(tags)
            else:
                self.timeline = self.timeline[i:]
                break

    def _add_edges(self, tags):
        for hashtag in tags:
            # increment vertex count to track number of distinct vertices
            self.vertices[hashtag] += 1

        for edge in itertools.combinations(tags, 2):
            # Edges pairs are sorted and therefore unique
            self.edges[edge] += 1

    def _remove_edges(self, tags):
        for hashtag in tags:
            if self.vertices[hashtag] > 1:
                self.vertices[hashtag] -= 1
            else:
                self.vertices.pop(hashtag)

        for edge in itertools.combinations(tags, 2):
            if self.edges[edge] > 1:
                self.edges[edge] -= 1
            else:
                self.edges.pop(edge)