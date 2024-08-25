def convert_to_nepali_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    if n < 1000:
        return ones[n // 100] + " hundred" + (" " + convert_to_nepali_words(n % 100) if n % 100 != 0 else "")
    if n < 100000:
        return convert_to_nepali_words(n // 1000) + " thousand" + (" " + convert_to_nepali_words(n % 1000) if n % 1000 != 0 else "")
    if n < 10000000:
        return convert_to_nepali_words(n // 100000) + " lakh" + (" " + convert_to_nepali_words(n % 100000) if n % 100000 != 0 else "")
    return convert_to_nepali_words(n // 10000000) + " crore" + (" " + convert_to_nepali_words(n % 10000000) if n % 10000000 != 0 else "")

def convert_to_words(num):
    number, decimal = str(float(num)).split(".")
    number_in_words = convert_to_nepali_words(int(number))
    if int(decimal) > 0:
        decimal_in_words = convert_to_nepali_words(int(decimal)).title()
        return number_in_words + " rupees and " + decimal_in_words + "paisa only"
    return number_in_words + " rupees only"


print(convert_to_words(200))
print(convert_to_nepali_words(15))
print(convert_to_nepali_words(5000))
print(convert_to_nepali_words(50000000))
