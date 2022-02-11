from collections import UserList
import re


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

child_user = "child_user"
child.add_user(child_user)
child.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users() #get the user
    if user in users:  #check if user is in the users 
        return True    #if yes than return true
    else:
        groups = group.get_groups()  # get the group from groups 
        for group in groups:  #loop through the groups list
            if is_user_in_group(user,group):   #check user in the group
                return True       #if so return true
    return False   #return false by default


print("----Test Case 1----\n")
print(is_user_in_group(sub_child_user, parent)) 
print("\n----Test Case 2----\n")
print(is_user_in_group("sub_child_user", child))
print("\n----Test Case 3----\n")
print(is_user_in_group(sub_child_user, sub_child))
print("\n----Test Case 4----\n")
print(is_user_in_group("sub_child", sub_child))