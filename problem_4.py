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


def is_user_in_group(user, group, checked_groups=set()):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
      checked_groups(set()): groups already checked (to prevent infinite recursion if any circular references)
    """

    if group.get_name() in checked_groups:
        return False

    # Check the users of the current group
    for groupMember in group.get_users():
        if groupMember == user:
            return True

    checked_groups.add(group.get_name())

    # Recurse to check the users of subgroups
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup, checked_groups):
            return True

    return False


"""
Sample Group Structure

    ----All Employees----
    |                   |
Managers        ----Engineers----
                |               |
            Manufacturing    Design

"""

all_employees = Group("AllEmployees")
all_employees.add_user("general_employee_1")
all_employees.add_user("general_employee_2")
all_employees.add_user("general_employee_3")

managers = Group("Managers")
managers.add_user("manager_1")
managers.add_user("manager_2")
managers.add_user("manager_3")

engineers = Group("AllEngineers")
engineers.add_user("general_engineer_1")
engineers.add_user("general_engineer_2")
engineers.add_user("general_engineer_3")

manufacturing_engineers = Group("ManufacturingEngineers")
manufacturing_engineers.add_user("me_user_1")
manufacturing_engineers.add_user("me_user_2")
manufacturing_engineers.add_user("me_user_3")

design_engineers = Group("DesignEngineers")
design_engineers.add_user("de_user_1")
design_engineers.add_user("de_user_2")
design_engineers.add_user("de_user_3")

engineers.add_group(manufacturing_engineers)
engineers.add_group(design_engineers)

engineers.add_group(all_employees)  # Added circular reference (not sure if needed to test against this case)

all_employees.add_group(engineers)
all_employees.add_group(managers)

# Test Case 1: User is in group
print(is_user_in_group("general_employee_1", all_employees))  # Expected: True

# Test Case 2: User is in sub-group
print(is_user_in_group("de_user_2", all_employees))  # Expected: True

# Test Case 3: User is not in group or subgroups
print(is_user_in_group("not_a_user", all_employees))  # Expected: False
