from common.ActionItem import ActionItem
from module.Student import Student
from data.Student import delStudent


# 添加学生
def delete():
    delStudent(Student.getInputStuno(False))
    print(f'学生[{stuno}]已经删除成功')


deleteAction = ActionItem('3', '删除学生信息', delete)
