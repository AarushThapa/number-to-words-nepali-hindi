def convert_to_nepali_words(n):
    ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + ones[n % 10]
    if n < 1000:
        return ones[n // 100] + "hundred" + convert_to_nepali_words(n % 100)
    if n < 100000:
        return convert_to_nepali_words(n // 1000) + "thousand" + convert_to_nepali_words(n % 1000)
    if n < 10000000:
        return convert_to_nepali_words(n // 100000) + "lakh" + convert_to_nepali_words(n % 100000)
    return convert_to_nepali_words(n // 10000000) + "crore" + convert_to_nepali_words(n % 10000000)


def convert_to_words(num):
    number, decimal = str(float(num)).split(".")
    number_in_words = convert_to_nepali_words(int(number)).title()
    if int(decimal) > 0:
        decimal_in_words = convert_to_nepali_words(int(decimal)).title()
        return number_in_words + " Rupees And " + decimal_in_words + "Paisa Only"
    return number_in_words + " Rupees Only"

