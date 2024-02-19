input_str=input()
split_=input_str.split()

x, y, w, h=int(split_[0]), int(split_[1]), int(split_[2]), int(split_[3])
dong,seo,nam,book=w-x, x, y, h-y
[dong,seo,nam,book]=[w-x, x, y, h-y]
print(min([dong,seo,nam,book]))