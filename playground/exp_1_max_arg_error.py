from politely import Styler


styler = Styler(strict=False)


sents = [
    "당신이 정말 놀라운 존재라는 것을 알아차리는 데 깃발이 필요하지 않아요.",
    "저는 그냥 당신 자체를 사랑해요."
]


for sent in sents:
    print(styler(sent, 0))

"""
네가 정말 놀라운 존재라는 것을 알아차리는 데 깃발이 필요하지 않다.
나는 그냥 너 자체를 사랑한다.
"""


for sent in sents:
    print(styler(sent, 2))

"""
당신이 정말 놀라운 존재라는 것을 알아차리는 데 깃발이 필요하지 않습니다.
저는 그냥 당신 자체를 사랑합니다.
"""



for sent in sents:
    print(styler(sent, 1))



