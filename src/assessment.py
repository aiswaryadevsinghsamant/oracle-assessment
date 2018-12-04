

# Given a string, write a function that returns a 'cleaned' string where adjacent chars
# that are the same have been reduced to a single char. So 'yyzzza' yields 'yza'.


def stringClean(dirty_string):
    from collections import OrderedDict
    cleaned_str_dict = OrderedDict()
    for d_str in dirty_string:
        cleaned_str_dict[d_str] = d_str
    if cleaned_str_dict:
        return ''.join(cleaned_str_dict)
    else:
        return None


# Given a string, return the length of the largest &quot;block&quot; in the string. A block is a run of
# adjacent chars that are the same.


def maxBlock(block_string):
    block_str_dict = dict()
    for d_str in block_string:
        if not block_str_dict.get(d_str):
            block_str_dict[d_str] = 1
        else:
            block_str_dict[d_str] = block_str_dict[d_str] + 1
    if not block_str_dict:
        return 0
    else:
        return (sorted(block_str_dict.values(), reverse=True))[0]


# Given a string, re-arrange the letters in acscending order.
def reorderBlock(unorderedBlock_str):
    if not unorderedBlock_str:
        return None
    else:
        return ''.join(sorted(sorted(unorderedBlock_str), key=str.upper))


from http import HTTPStatus
from flask import Flask, request, make_response

app = Flask(__name__)

HTTP_FUNC_NAME = 'HTTP_FUNC_NAME'
HTTP_FUNC_VAL = 'HTTP_FUNC_VAL'


@app.route("/invoke-function", methods=['GET'])
def invokeFunction():
    try:
        func_name = request.headers.environ.get(HTTP_FUNC_NAME, None)
        func_val = request.headers.environ.get(HTTP_FUNC_VAL, None)
        rslt = None
        if 'stringClean' == func_name:
            rslt = stringClean(func_val)
        elif 'maxBlock' == func_name:
            rslt = maxBlock(func_val)
        elif 'reorderBlock' == func_name:
            rslt = reorderBlock(func_val)
        else:
            return make_response('Invalid Request for method {}, invoked for val {}'.format(func_name, func_val), HTTPStatus.BAD_REQUEST)
        return make_response(str(rslt), HTTPStatus.OK)
    except:
        return make_response('Opps! I did again', HTTPStatus.INTERNAL_SERVER_ERROR)

if __name__ == "__main__":
    app.run()

