# Created by: Hiab G
# Date: Wed, APRIL. 3RD
# This program checks if a year is a leap year


def main():
    # Get the player's guess
    try:

        year_as_string = int(input("Enter the year: "))

        if year_as_string % 4 == 0:
            if year_as_string % 100 == 0:
                if year_as_string % 400 == 0:
                    print(f"THIS IS A LEAP YEAR")

                else:
                    print(f"THIS IS NOT A LEAP YEAR")
            else:
                print(f"THIS IS  A LEAP YEAR")
        else:
            print(f"THIS IS NOT A LEAP YEAR")

    # checks if a the input is valid
    except Exception:
        year_as_string = input("")
        print(f"Please enter a valid year, {year_as_string} is not a valid year.")

    finally:
        print(f"THANK YOU FOR PLAYING!")


if __name__ == "__main__":
    main()
