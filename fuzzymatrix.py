'fuzzymatrix'


class FuzzyMatrix:
    'Fuzzy Matrix object | 模糊矩阵对象 | FuzzyMatrix(value: list[list[float]])'

    def __init__(self, value: list[list[float]] = [[0]]) -> None:
        if type(value) != list:
            raise ValueError('Must be a list | 必须是一个列表')
        if type(value[0]) == list:
            width = len(value[0])
        else:
            width = len(value)
            value = [value]
        for y in value:
            if type(value) != list or len(y) != width:
                raise ValueError('Format error | 格式错误')
            for x in y:
                if type(x) != int and type(x) != float or x < 0 or x > 1:
                    raise ValueError(
                        'Membership must be between 0 and 1 | 隶属度必须介于0和1之间')
        self._value = value

    @property
    def value(self) -> list:
        'Get fuzzy matrix value | 获取模糊矩阵值'
        return self._value

    @property
    def width(self) -> int:
        'Get fuzzy matrix width | 获取模糊矩阵宽度'
        return len(self._value[0])

    @property
    def height(self) -> int:
        'Get fuzzy matrix height | 获取模糊矩阵高度'
        return len(self._value)

    @property
    def T(self) -> 'FuzzyMatrix':
        'Transpose | 转置'
        return FuzzyMatrix([[self._value[y][x] for y in range(self.height)] for x in range(self.width)])

    @property
    def N(self) -> 'FuzzyMatrix':
        'Negative | 取反'
        return FuzzyMatrix([[1 - self._value[y][x] for x in range(self.width)] for y in range(self.height)])

    def row(self, y: int) -> list:
        'Get fuzzy matrix row | 获取模糊矩阵行'
        return self._value[y]

    def column(self, x: int) -> list:
        'Get fuzzy matrix column | 获取模糊矩阵列'
        return [self._value[y][x] for y in range(self.height)]

    def element(self, x: int, y: int) -> float | int:
        'Get fuzzy matrix element | 获取模糊矩阵元素'
        return self._value[y][x]

    def reset_width(self, width: int) -> None:
        'Reset fuzzy matrix width | 重置模糊矩阵宽度'
        if self.width != 1:
            raise ValueError(
                'Only fuzzy matrices with width 1 can be reset | 仅可重设宽度为 1 的模糊矩阵')
        return FuzzyMatrix([i * width for i in self._value])

    def reset_height(self, height: int) -> None:
        'Reset fuzzy matrix height | 重置模糊矩阵高度'
        if self.height != 1:
            raise ValueError(
                'Only fuzzy matrices with height 1 can be reset | 仅可重设高度为 1 的模糊矩阵')
        return FuzzyMatrix(self._value * height)

    def set_row(self, y: int, value: list) -> None:
        'Set fuzzy matrix row | 设置模糊矩阵行'
        if len(value) != self.width:
            raise ValueError('Format error | 格式错误')
        for x in value:
            if type(x) != int and type(x) != float or x < 0 or x > 1:
                raise ValueError(
                    'Membership must be between 0 and 1 | 隶属度必须介于0和1之间')
        self._value[y] = value

    def set_column(self, x: int, value: list) -> None:
        'Set fuzzy matrix column | 设置模糊矩阵列'
        if len(value) != self.height:
            raise ValueError('Format error | 格式错误')
        for y in value:
            if type(y) != int and type(y) != float or y < 0 or y > 1:
                raise ValueError(
                    'Membership must be between 0 and 1 | 隶属度必须介于0和1之间')
        for y in range(self.height):
            self._value[y][x] = value[y]

    def set_element(self, x: int, y: int, value: float) -> None:
        'Set fuzzy matrix element | 设置模糊矩阵元素'
        if value < 0 or value > 1:
            raise ValueError(
                'Membership must be between 0 and 1 | 隶属度必须介于0和1之间')
        self._value[y][x] = value


def printFuzzyMatrix(matrix: 'FuzzyMatrix', maxRound: int = 4) -> str:
    'Format print and return fuzzy matrix | 格式化打印并返回模糊矩阵'
    if maxRound < 1:
        raise ValueError('maxRound must be greater than 1 | maxRound必须大于1')
    value = matrix.value
    res = '\n'.join([' '.join(['{:>{}}'.format(
        float(round(x, maxRound)), maxRound + 3) for x in row]) for row in value])
    width = len(value[0])
    height = len(value)
    print('\n{} x {} FuzzyMatrix:'.format(width, height))
    print('-' * (width * (maxRound + 4) + 1) + '\n' + res +
          '\n' + '-' * (width * (maxRound + 4) + 1) + '\n')
    return res


def create(width: int = 1, height: int = 1, value: float = 0.0) -> 'FuzzyMatrix':
    'Create a fuzzy matrix | 创建一个模糊矩阵'
    if value < 0 or value > 1:
        raise ValueError('Membership must be between 0 and 1  |  隶属度必须介于0和1之间')
    return FuzzyMatrix([[value for x in range(width)] for y in range(height)])


def inputRow(prompt: object = 'Enter a single row fuzzy matrix | 请输入单行模糊矩阵: ') -> 'FuzzyMatrix':
    'Enter a single row fuzzy matrix | 输入单行模糊矩阵'
    row = input(prompt).split()
    if len(row) == 0:
        raise ValueError('Format error  |  格式错误')
    return FuzzyMatrix([float(x) for x in row])


def inputFuzzyMatrix(x: int, y: int, prompt: object = ...) -> 'FuzzyMatrix':
    'Enter a fuzzy matrix | 输入模糊矩阵'
    if prompt == ...:
        prompt = 'Enter a {} x {} fuzzy matrix | 请输入一个 {} x {} 的模糊矩阵: '.format(
            x, y, x, y)
    print(prompt)
    value = []
    for i in range(y):
        row = input('Enter line {} | 请输入第 {} 行: '.format(i, i)).split()
        if len(row) != x:
            raise ValueError('Format error | 格式错误')
        value.append([float(x) for x in row])
    return FuzzyMatrix(value)


# def aslfjg(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> bool:
#     if matrix1.width == matrix2.width and matrix1.height == matrix2.height:
#         return True
#     elif matrix1.width == 1 and matrix1.height == matrix2.height:
#         matrix1 = matrix1.reset_width(matrix2.width)
#         return True
#     elif matrix1.width == matrix2.width and matrix1.height == 1:
#         matrix1 = matrix1.reset_height(matrix2.height)
#         return True
#     else:
#         return False

def conjunction(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
    'Conjunction of fuzzy matrices | 模糊矩阵的合取'
    def _conjunction(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
        value = []
        for y in range(matrix1.height):
            value.append([])
            for x in range(matrix1.width):
                value[y].append(
                    min(matrix1.element(x, y), matrix2.element(x, y)))
        return FuzzyMatrix(value)
    if matrix1.width == matrix2.width and matrix1.height == matrix2.height:
        pass
    elif matrix1.width == 1 and matrix1.height == matrix2.height:
        matrix1 = matrix1.reset_width(matrix2.width)
    elif matrix2.width == 1 and matrix2.height == matrix1.height:
        matrix2 = matrix2.reset_width(matrix1.width)
    elif matrix1.width == matrix2.width and matrix1.height == 1:
        matrix1 = matrix1.reset_height(matrix2.height)
    elif matrix2.width == matrix1.width and matrix2.height == 1:
        matrix2 = matrix2.reset_height(matrix1.height)
    elif matrix1.width == 1 and matrix2.height == 1:
        matrix1 = matrix1.reset_width(matrix2.width)
        matrix2 = matrix2.reset_height(matrix1.height)
    elif matrix1.height == 1 and matrix2.width == 1:
        matrix1 = matrix1.reset_height(matrix2.height)
        matrix2 = matrix2.reset_width(matrix1.width)
    else:
        raise ValueError('Format error | 格式错误')
    return _conjunction(matrix1, matrix2)

    # if not (aslfjg(matrix1, matrix2) or aslfjg(matrix2, matrix1)):
    #     raise ValueError('Format error | 格式错误')
    # return _conjunction(matrix1, matrix2)


def disjunction(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
    'Disjunction of fuzzy matrix | 模糊矩阵的析取'
    def _disjunction(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
        value = []
        for y in range(matrix1.height):
            value.append([])
            for x in range(matrix1.width):
                value[y].append(
                    max(matrix1.element(x, y), matrix2.element(x, y)))
        return FuzzyMatrix(value)
    if matrix1.width == matrix2.width and matrix1.height == matrix2.height:
        pass
    elif matrix1.width == 1 and matrix1.height == matrix2.height:
        matrix1 = matrix1.reset_width(matrix2.width)
    elif matrix2.width == 1 and matrix2.height == matrix1.height:
        matrix2 = matrix2.reset_width(matrix1.width)
    elif matrix1.width == matrix2.width and matrix1.height == 1:
        matrix1 = matrix1.reset_height(matrix2.height)
    elif matrix2.width == matrix1.width and matrix2.height == 1:
        matrix2 = matrix2.reset_height(matrix1.height)
    elif matrix1.width == 1 and matrix2.height == 1:
        matrix1 = matrix1.reset_width(matrix2.width)
        matrix2 = matrix2.reset_height(matrix1.height)
    elif matrix1.height == 1 and matrix2.width == 1:
        matrix1 = matrix1.reset_height(matrix2.height)
        matrix2 = matrix2.reset_width(matrix1.width)
    else:
        raise ValueError('Format error | 格式错误')
    return _disjunction(matrix1, matrix2)


def composition(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
    'Composition of fuzzy matrix | 模糊矩阵的合成'
    def _composition(x: int, y: int) -> float:
        ls = []
        for i in range(matrix1.width):
            ls.append(min(matrix1.element(i, y), matrix2.element(x, i)))
        return max(ls)
    if matrix1.width != matrix2.height:
        raise ValueError('Format error | 格式错误')
    value = []
    for y in range(matrix1.height):
        value.append([])
        for x in range(matrix2.width):
            value[y].append(_composition(x, y))
    return FuzzyMatrix(value)


o = composition


def zadeh(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
    'Zadeh inference | Zadeh 推理法'
    return disjunction(conjunction(matrix1.T, matrix2), matrix1.T.N)


def mandani(matrix1: 'FuzzyMatrix', matrix2: 'FuzzyMatrix') -> 'FuzzyMatrix':
    'Mandani inference | Mandani 推理法'
    return conjunction(matrix1.T, matrix2)


if __name__ == 'fuzzymatrix':
    pass

if __name__ == '__main__':
    pass
