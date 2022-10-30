
"""
    Verilən ölçülərə əsasən duzbucaqlinin sahəsini hesablayın:
        En = 7.5
        Uzunluq = 9
        Sahe = ?
"""


def main():
    length = abs(float(input("length:")))
    width = abs(float(input("width:")))
    #length, width = map(float, input("").split())
    area = (length) * width
    print(f"Area: {area:.2f}")

if __name__ == "__main__":
    main()
