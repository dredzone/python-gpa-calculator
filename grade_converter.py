gpa_scale = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,

    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,

    "C+": 2.33,
    "C": 2.0,
    "C-": 1.67,

    "D+": 1.33,
    "D": 1.0,
    "D-": 0.67,

    "F+": 0.0,
    "F": 0.0,
    "F-": 0.0,
}


def grade_converter(grade, scale='Regular'):
    if grade in gpa_scale:
        gpa = gpa_scale.get(grade)
        match scale.upper():
            case "REGULAR":
                return gpa
            case "HONORS":
                return gpa + 0.5
            case "AP":
                return gpa + 1.0
            case default:
                return gpa
    else:
        return -1
