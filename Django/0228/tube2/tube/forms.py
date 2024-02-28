from django import forms


class CommentForm:
    # 사용자로부터 문자열 형태의 데이터를 받음
    # widget=forms.Textarea -> 여러 줄의 텍스트를 입력 받는다
    message = forms.CharField(widget=forms.Textarea)
