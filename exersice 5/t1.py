class Kharchang:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        second_dna = self.dna[:10]
        self.dna += second_dna
        self.dna = self.dna.replace("tt", "o")
        return self.dna


class BabEsfanji(Kharchang):
    def process_dna(self):
        sorted22 = self.merge_sort(str(len(self.dna)))
        sorted22 = "".join(sorted22)
        sorted22 = int(sorted22) + 100
        return(sorted22)

    def merge_sort(self, dna):
         if len(dna) <= 1:
            return dna

         mid = len(dna) // 2
         left_half = dna[:mid]
         right_half = dna[mid:]

         left_half = self.merge_sort(left_half)
         right_half = self.merge_sort(right_half)

         return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


class Akhtapos:
    def __init__(self, dna):
        self.dna = dna

    def process_dna(self):
        i = 0
        jef = 0
        counter = 0
        new_dna = ''
        while i < len(self.dna) - 2:
            if self.dna[i] == "x" and counter == 0:
                jef = i - 6
                counter += 1
            if self.dna[i] == self.dna[i + 1] == self.dna[i + 2]:
                self.dna = self.dna[:i] + "(0_0)" + self.dna[i + 3:]
                i += 3
            else:
                i += 1
        if counter == 1:
            result = self.dna + str(jef)
        else:
            result = self.dna
        return result

def main():
    data = input().strip()
    if data.startswith("m"):
        character = Kharchang(data[0:])
    elif data.startswith("sb"):
        character = BabEsfanji(data[0:])
    elif data.startswith("s") :
        character = Akhtapos(data[0:])
    elif data[len(data) - 1] == "m":
        data = data[::-1]
        character = Kharchang(data)
    elif data[len(data) - 1] == "s" and data[len(data) - 2] == "b":
        data = data[::-1]
        character = BabEsfanji(data)
    elif data[len(data) - 1] == "s" and data[len(data) - 2] != "b":
        data = data[::-1]
        character = Akhtapos(data)
    else: 
        print('invalid input')
        return
    
    result = character.process_dna()
    print(result)

if __name__ == "__main__":
    main()