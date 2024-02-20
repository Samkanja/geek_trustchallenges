from src.program_charges import ProgramCharges


def check_matches(program, qty):
    program_lst, program_counts, program_costs = [], [], []
    match program:
        case "CERTIFICATION":
            price = getattr(ProgramCharges, program)
            program_costs.append(price)
            program_counts.append(qty)
            program_lst.append(program)
        case "DEGREE":
            price = getattr(ProgramCharges, program)
            program_costs.append(price)
            program_counts.append(qty)
            program_lst.append(program)

        case "DIPLOMA":
            price = getattr(ProgramCharges, program)
            program_costs.append(price)
            program_counts.append(qty)
            program_lst.append(program)
    return program_costs, program_lst, program_counts
