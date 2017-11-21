import random

messages = ['是',
  '没错',
  '说的对',
  '深表赞同',
  '精辟的论断',
  '简直无懈可击',
  '佩服到五体投地',
  '智商超出本机范围'
]

inputMessage=input()

print(messages[(len(inputMessage)-1)%8])
