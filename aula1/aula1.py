"""
Exercício 1 de Mentoria de Python Web - Lead Mentoring 2.0
Mentor: Gustavo Soares
Mentorados: Jhonnas ChristianNobre
            Joshuel Nobre

Atividade: Manipulação de Arquivos
"""

import re
from pathlib import Path
from typing import List, Union
from tabulate import tabulate

title = """ACME Inc.\t\tUso do espaço em disco pelos usuários
--------------------------------------------------------------
"""
header = ["Nr. ", "Usuários", "Espaço utilizado", "% do uso"]

footer = """\n
Espaço total ocupado: {total} MB
Espaço médio ocupado: {avg} MB
"""


def read_file(path: Union[str, Path]) -> List[str]:
    with open(path, "r+") as f:
        return f.readlines()


def clear_data(data: List[str]) -> List[list]:
    return [[
        i+1,
        data[i][:15].strip(),
        f"{convert_bytes_to_mbytes(int(data[i][16:].strip()))} MB",
    ] for i in range(len(data))]


def convert_bytes_to_mbytes(data_bytes: int) -> float:
    return round(data_bytes / 1024**2, 2)


def calc_used_space(data_bytes: str, total: Union[int, float]):
    data_bytes = float(re.sub(r"[a-zA-Z]", "", data_bytes))
    return round(data_bytes * 100 / total, 2)


def calc_total(data: List[list]) -> Union[int, float]:
    return sum([
        float(re.sub(r"[a-zA-Z]", "", d[2]))
        for d in data
    ])

def calc_avg(total: Union[int, float], qtd: int) -> Union[int, float]:
    return round(total / qtd, 2)



def render_data_to_string(data: List[list], **kwargs) -> str:
    assert kwargs.get("total") != None, "total keyword is required"
    assert kwargs.get("avg") != None, "avg keyword is required"

    table = tabulate(data, headers=header, tablefmt="plain")
    _footer = footer.format(total=kwargs.get("total"), avg=kwargs.get("avg"))
    return title + table + _footer

def write_file(
    path: Union[Path, str],
    data: str,

) -> None:
    with open(path, "w+") as f:
        f.write(data)


def main():
    dirt_users = read_file("usuarios.txt")
    print("dirt_users", dirt_users)
    cleaned_users = clear_data(dirt_users)
    print("cleaned_users", cleaned_users)
    total = calc_total(cleaned_users)
    avg = calc_avg(total, len(cleaned_users))

    final_data = [
        [*data, f"{calc_used_space(data[2], total)} %"]
        for data in cleaned_users
    ]
    print("final_data", final_data)
    rendered_data = render_data_to_string(
        data=final_data,
        total=total,
        avg=avg
    )
    print("\nPreview result:\n")
    print(rendered_data)
    write_file("relatorio.txt", rendered_data)


if __name__ == "__main__":
    main()
