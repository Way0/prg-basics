###
    # Calculates the final grade for a test based
    # on the number of points obtained
    #
def pts_to_grade(points):

    if points >= 18:
        grade = 'Excellent'
    elif points >= 15. and points < 18:
        grade = 'Good'
    elif points >= 12 and points < 15:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'

    return grade

test_result = 15

final_grade = pts_to_grade(test_result)

print('You scored {} points on the test. Your final grade is {}'.format(test_result, final_grade))


