from django.core.exceptions import ValidationError

# '#'이 들어있는지 검증
def validate_no_hash(value):
    if "#" in value:
        raise ValidationError("'#'이 들어갈 수 없습니다.")

# 숫자가 들어있는지 검증
def validate_no_numbers(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError("숫자가 들어갈 수 없습니다")

# 입력된 값이 0부터 10 사이의 숫자인지 검증
def validate_score(value):
    if value < 0 or value > 10:
        raise ValidationError("'0부터 10 사이의 숫자만 들어갈 수 있습니다.")