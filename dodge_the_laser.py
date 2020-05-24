
def solution(s):
    def floor_root_2(x):
        sqrt_2 = int(
            "41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206")
        ten_power = int(
            "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        ret = int((x * (x + 1)) / 2)
        if x <= 10:
            for i in range(x):
                ret += int((sqrt_2 * (i + 1)) / ten_power)
            return ret
        last_term = int((sqrt_2 * x) / ten_power)
        ret += (x * last_term) - int((last_term * (last_term + 1)) / 2) - floor_root_2(last_term)
        return ret

    return str(floor_root_2(int(s)))


if __name__ == "__main__":
    print("4208", solution("77"))
    print("19", solution("5"))
