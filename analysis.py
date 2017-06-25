import Novels
import math, json

def tfjson(novel, outputFile):
    TF_Output = open(outputFile,"w")
    book = Novels.Novel(novel)

    bookImage = book.term_frenquency()

    sortedImage = []
    for item in bookImage.items():
        sortedImage.append((item[0],item[1]))
    for i in range(0,len(sortedImage)-1):
        for j in range(i+1,len(sortedImage)-1):
            if sortedImage[i][1] < sortedImage[j][1]:
                t = sortedImage[i]
                sortedImage[i] = sortedImage[j]
                sortedImage[j] = t
    TF_Output.write("{")
    for i in range(0, 100):
        print(sortedImage[i])

        TF_Output.write("\""+sortedImage[i][0]+"\" :"+str(sortedImage[i][1])+",\n")

    TF_Output.write("}")
    TF_Output.close()
    book.close_novel()
    return sortedImage


def tf_idf(novelList):
    bookImageList = [Novels.Novel(novel).term_frenquency() for novel in novelList]

    for bookImage in bookImageList:
        # print(bookImage)
        for word in bookImage:
            numerator = len(novelList)
            denominator = 0
            for otherBookImage in bookImageList:
                if otherBookImage.__contains__(word):
                    denominator += 1
            idf = math.log(numerator/denominator)

            bookImage[word] *= idf

    return bookImageList

# output = open("tf_idf.csv","w")
# output.write("word,tf-idf,book\n")
# bookList = ["war_peace.txt","test.txt"]
# bookImageList = tf_idf(bookList)
# book_id = 0
# print(bookList)
# for bookImage in bookImageList:
#     sortedImage = []
#     for item in bookImage.items():
#         sortedImage.append((item[0],item[1]))
#     for i in range(0,len(sortedImage)-1):
#         for j in range(i+1,len(sortedImage)-1):
#             if sortedImage[i][1] < sortedImage[j][1]:
#                 t = sortedImage[i]
#                 sortedImage[i] = sortedImage[j]
#                 sortedImage[j] = t
#     for item in bookImage.items():
#         if item[1] > 0:
#             output.write(item[0]+",")
#             output.write(str(item[1])+",")
#             output.write(bookList[book_id]+"\n")
#     book_id += 1

output = open("war_peace_grades.json","w+")
book = Novels.Novel("war_peace.txt")
rm = book.relational_matrix()
output.write(json.dumps(rm))
output.close()
