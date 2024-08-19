"""
This module extends the MilestoneNoResponseDcrGraph class to include support for
nested groups and subprocesses within Dynamic Condition Response (DCR) Graphs.

The module adds functionality to handle hierarchical structures in DCR Graphs,
allowing for more complex process models with nested elements and subprocesses.

Classes:
    GroupSubprocessDcrGraph: Extends MilestoneNoResponseDcrGraph to include nested groups and subprocesses.

This class provides methods to manage and manipulate nested groups and subprocesses
within a DCR Graph, enhancing the model's ability to represent complex organizational
structures and process hierarchies.
"""
from pm4py.objects.dcr.milestone_noresponse.obj import MilestoneNoResponseDcrGraph
from typing import Set, Dict


class GroupSubprocessDcrGraph(MilestoneNoResponseDcrGraph):
    """
    This class extends the MilestoneNoResponseDcrGraph to include nested groups
    and subprocesses, allowing for more complex hierarchical structures in DCR Graphs.

    Attributes
    ----------
    self.__nestedgroups: Dict[str, Set[str]]
        A dictionary mapping group names to sets of event IDs within each group.
    self.__subprocesses: Dict[str, Set[str]]
        A dictionary mapping subprocess names to sets of event IDs within each subprocess.
    self.__nestedgroups_map: Dict[str, str]
        A dictionary mapping event IDs to their corresponding group names.

    Methods
    -------
    obj_to_template(self) -> dict:
        Converts the object to a template dictionary, including nested groups and subprocesses.

    """
    def __init__(self, template=None):
        super().__init__(template)
        self.__nestedgroups = {} if template is None else template['nestedgroups']
        self.__subprocesses = {} if template is None else template['subprocesses']
        self.__nestedgroups_map = {} if template is None else template['nestedgroupsMap']
        if len(self.__nestedgroups_map) == 0 and len(self.__nestedgroups) > 0:
            self.__nestedgroups_map = {}
            for group, events in self.__nestedgroups.items():
                for e in events:
                    self.__nestedgroups_map[e] = group

    def obj_to_template(self):
        res = super().obj_to_template()
        res['nestedgroups'] = self.__nestedgroups
        res['subprocesses'] = self.__subprocesses
        res['nestedgroupsMap'] = self.__nestedgroups_map
        return res

    @property
    def nestedgroups(self) -> Dict[str, Set[str]]:
        return self.__nestedgroups

    @nestedgroups.setter
    def nestedgroups(self, ng):
        self.__nestedgroups = ng

    @property
    def nestedgroups_map(self) -> Dict[str, str]:
        return self.__nestedgroups_map

    @nestedgroups_map.setter
    def nestedgroups_map(self, ngm):
        self.__nestedgroups_map = ngm

    @property
    def subprocesses(self) -> Dict[str, Set[str]]:
        return self.__subprocesses

    @subprocesses.setter
    def subprocesses(self, sps):
        self.__subprocesses = sps
