{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "TerceiraAula.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cCaM5sZ7BFHB"
      },
      "source": [
        "# Condicionais\r\n",
        "\r\n",
        "Principal forma de atribuir uma lógica ao nosso código.\r\n",
        "\r\n",
        "Só executa códigos que corresponderem a condição especificada.\r\n",
        "\r\n",
        "Ex:\r\n",
        "\r\n",
        "Se estiver quente\r\n",
        "*   Tomar Sorvete\r\n",
        "*   Vamos para Praia\r\n",
        "\r\n",
        "Se estiver frio\r\n",
        "*   Comer Chocolate\r\n",
        "*   Vamos ao cinema\r\n",
        "\r\n",
        "\r\n",
        "Condições:\r\n",
        "- Igualdade == \r\n",
        "- Menor <\r\n",
        "- Maior >\r\n",
        "- Menor Igual <=\r\n",
        "- Maior Igual >=\r\n",
        "- Diferente !=\r\n",
        "\r\n",
        "\r\n",
        "\r\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GYYX4Gmp_QIy",
        "outputId": "b33f10f0-2270-4b3c-d30c-1490d57a6355"
      },
      "source": [
        "temperatura = 'frio'\r\n",
        "\r\n",
        "if temperatura == 'quente':\r\n",
        "  print('Vamos tomar sorvete de flocos!')\r\n",
        "  print('Vamos para a praia')\r\n",
        "else:\r\n",
        "  print('Vamos comer chocolate')\r\n",
        "  print('Vamos ao cinema')"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Vamos comer chocolate\n",
            "Vamos ao cinema\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eVBfuN8oB4UT",
        "outputId": "3aed0c3a-78c2-495b-a2b2-05335e70d317"
      },
      "source": [
        "numero = 20\r\n",
        "\r\n",
        "if numero <= 20:\r\n",
        "  print('É um número pequeno')\r\n",
        "else:\r\n",
        "  print('É um número grande')"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "É um número pequeno\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jtKDtcP9Crgv",
        "outputId": "06528545-47de-4922-d85e-1b0af9dce800"
      },
      "source": [
        "nome = 'paulo'\r\n",
        "\r\n",
        "if nome != 'felipe':\r\n",
        "  print('Cade o Felipe?') \r\n",
        "elif nome == 'felipe':\r\n",
        "  print('É o Felipe')"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cade o Felipe?\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8w9icw6kC1nV",
        "outputId": "d8002f70-8246-46b5-b813-ae3676f33207"
      },
      "source": [
        "# 1, 3, 5\r\n",
        "\r\n",
        "numero = 7\r\n",
        "\r\n",
        "if numero == 1:\r\n",
        "  print('Você ganhou')\r\n",
        "elif numero == 3:\r\n",
        "  print('Você ganhou')\r\n",
        "elif numero == 5:\r\n",
        "  print('Você ganhou')\r\n",
        "else:\r\n",
        "  print('Você perdeu!')"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Você perdeu!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4wV4n526DtNb",
        "outputId": "3d2e936f-bc80-45f0-9bf0-afa91cd7ff05"
      },
      "source": [
        "nome = 'felipe'\r\n",
        "sobrenome = 'santos'\r\n",
        "\r\n",
        "if nome == 'felipe':\r\n",
        "  if sobrenome == 'cabrera':\r\n",
        "    print('É o Felipe Cabrera!')\r\n",
        "  else:\r\n",
        "    print('É outro Felipe!')\r\n",
        "else:\r\n",
        "  print('Não é o Felipe Cabrera!')"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "É outro Felipe!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_e0fPIfxFaNG",
        "outputId": "77499d48-05e9-4464-c2f1-6590b172ef40"
      },
      "source": [
        "# 1, 3, 5, 7, 9\r\n",
        "\r\n",
        "numero = 8\r\n",
        "\r\n",
        "if numero == 1:\r\n",
        "  print('Você ganhou')\r\n",
        "elif numero == 3:\r\n",
        "  print('Você ganhou')\r\n",
        "elif numero == 5:\r\n",
        "  print('Você ganhou')\r\n",
        "elif numero == 7:\r\n",
        "  print('Você ganhou')\r\n",
        "elif numero == 9:\r\n",
        "  print('Você ganhou')\r\n",
        "else:\r\n",
        "  print('Você perdeu!')"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Você perdeu!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2evLIXwUFgnh",
        "outputId": "e902aae5-393d-4d9a-f531-3d0c5c499882"
      },
      "source": [
        "nome = 'felipe'\r\n",
        "sobrenome = 'cabrera'\r\n",
        "idade = 24\r\n",
        "\r\n",
        "if nome == 'felipe':\r\n",
        "  if sobrenome == 'cabrera':\r\n",
        "      if idade == 24:\r\n",
        "        print('É o Felipe Cabrera da ByLearn!')\r\n",
        "      else:\r\n",
        "        print('É outro Felipe Cabrera')\r\n",
        "  else:\r\n",
        "    print('É outro Felipe!')\r\n",
        "else:\r\n",
        "  print('Não é o Felipe Cabrera!')"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "É o Felipe Cabrera da ByLearn!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Y-oWxwpcGE6G"
      },
      "source": [
        "# Operadores Lógicos\r\n",
        "\r\n",
        "Servem para utilizar condições Compostas.\r\n",
        "\r\n",
        "Uma condição E (**and**) outra condição\r\n",
        "\r\n",
        "*   Todas devem ser verdadeiras\r\n",
        "\r\n",
        "Uma condição OU (**or**) outra condição\r\n",
        "\r\n",
        "*   Ao menos uma  "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PJwyAAPMFyK5",
        "outputId": "2208126b-298b-4fb3-857f-b2e108e863bb"
      },
      "source": [
        "# 1, 3, 5, 7 ou 9\r\n",
        "\r\n",
        "numero = 8\r\n",
        "\r\n",
        "if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9:\r\n",
        "  print('Você Ganhou!')\r\n",
        "else:\r\n",
        "  print('Você Perdeu!')\r\n",
        "\r\n"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Você Perdeu!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6cTHnbwLGyZG",
        "outputId": "ec888272-dab6-4e17-909d-c905e129822a"
      },
      "source": [
        "nome = 'felipe'\r\n",
        "sobrenome = 'cabrera'\r\n",
        "idade = 24\r\n",
        "\r\n",
        "if nome == 'felipe' and sobrenome == 'cabrera' and idade == 24:\r\n",
        "  print('É o Felipe Cabrera da ByLearn')\r\n",
        "else:\r\n",
        "  print('É outra pessoa')"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "É o Felipe Cabrera da ByLearn\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "triX2PaNHNIx",
        "outputId": "72186607-c498-497f-be09-8b72e1fce273"
      },
      "source": [
        "# 1, 3 ou 5\r\n",
        "# Nome = Felipe\r\n",
        "\r\n",
        "nome = 'felipe'\r\n",
        "numero = 5\r\n",
        "\r\n",
        "if nome == 'felipe' and (numero == 1 or numero == 3 or numero == 5):\r\n",
        "  print('O Felipe escolheu o número certo')\r\n",
        "else:\r\n",
        "  print('Erro!')"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O Felipe escolheu o número certo\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zj-Y1AMJICj0",
        "outputId": "8e002c06-6eb3-4369-db04-27a30b1b2646"
      },
      "source": [
        "numeros_aceitos = [1, 3, 5, 7, 9]\r\n",
        "\r\n",
        "numero = 6\r\n",
        "\r\n",
        "if numero in numeros_aceitos:\r\n",
        "  print('Você Ganhou!')\r\n",
        "else:\r\n",
        "  print('Você Perdeu!')"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Você Perdeu!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XeNKebWkIpxm",
        "outputId": "049cd980-1e06-4ced-9de3-990a97370f19"
      },
      "source": [
        "nome = 'Felipe'\r\n",
        "sobrenome = 'Cabrera'\r\n",
        "idade = 24\r\n",
        "\r\n",
        "if nome.lower() == 'felipe' and sobrenome.lower() == 'cabrera' and idade == 24:\r\n",
        "  print('É o Felipe Cabrera da ByLearn')\r\n",
        "else:\r\n",
        "  print('É outra pessoa')"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "É o Felipe Cabrera da ByLearn\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6ecXV4qAJbNO"
      },
      "source": [
        "# Laços de Repetição\r\n",
        "\r\n",
        "\r\n",
        "Forma de evitar a repetição de código, executando uma ação repetidas vezes"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pyi_TMagI_0D"
      },
      "source": [
        "# Todos os números até 10 =>  0 ... 9  \r\n",
        "# Mínimo é Inclusivo => Exite\r\n",
        "# Máximo é Exclusivo => Não Existe\r\n",
        "print(0)\r\n",
        "print(1)\r\n",
        "print(2)\r\n",
        "print(3)\r\n",
        "print(4)\r\n",
        "print(5)\r\n",
        "print(6)\r\n",
        "print(7)\r\n",
        "print(8)\r\n",
        "print(9)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cjoP3I9mJ5nS"
      },
      "source": [
        "# for variavel in sequencia/lista:\r\n",
        "for numero in range(11):\r\n",
        "  print(numero)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "76k4yLaCKZZj"
      },
      "source": [
        "# for variavel in sequencia:\r\n",
        "\r\n",
        "# PARA CADA variavel NA MINHA sequencia:\r\n",
        "    # executar uma repetição (código) => Iteração\r\n",
        "\r\n",
        "# PARA CADA numero NA MINHA sequencia de números até 10:\r\n",
        "  # mostrar o numero \r\n",
        "\r\n",
        "for numero in range(10):\r\n",
        "   print('O número atual é:', numero)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "304xw89ZKf6m",
        "outputId": "6d0acee7-0a86-45d6-c83c-2d825867173c"
      },
      "source": [
        "# 3 ~ [8] \r\n",
        "for numero in range(3,9):\r\n",
        "  print(numero)"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JzSx4i9hLTCW",
        "outputId": "237a6758-ab4a-42ac-880d-ef78e1e644dc"
      },
      "source": [
        "for numero in range(3, 16, 2):\r\n",
        "  print(numero)"
      ],
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n",
            "5\n",
            "7\n",
            "9\n",
            "11\n",
            "13\n",
            "15\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-ppVGcBDLac0"
      },
      "source": [
        "resto_divisao = 9 % 2"
      ],
      "execution_count": 54,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-qNpHW-KLxDM",
        "outputId": "e5b43dcf-95bd-43aa-de77-1de370521a44"
      },
      "source": [
        "resto_divisao"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_2tTSEtaLyta",
        "outputId": "5e7ad4b4-c763-40b2-9a7b-274c2211b650"
      },
      "source": [
        "for numero in range(1, 11):\r\n",
        "  if numero % 2 == 0:\r\n",
        "    print(f'O número {numero} é par!')\r\n",
        "  if numero % 2 == 1:\r\n",
        "    print(f'O número {numero} é impar!')"
      ],
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O número 1 é impar!\n",
            "O número 2 é par!\n",
            "O número 3 é impar!\n",
            "O número 4 é par!\n",
            "O número 5 é impar!\n",
            "O número 6 é par!\n",
            "O número 7 é impar!\n",
            "O número 8 é par!\n",
            "O número 9 é impar!\n",
            "O número 10 é par!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2EGhX2LiMPqp",
        "outputId": "9a56a638-7518-40af-b967-cb64956cd564"
      },
      "source": [
        "for numero in range(1, 11):\r\n",
        "  if numero % 2 == 0:\r\n",
        "    print(f'O número {numero} é par!')\r\n",
        "  else:\r\n",
        "    print(f'O número {numero} é impar')"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O número 1 é impar\n",
            "O número 2 é par!\n",
            "O número 3 é impar\n",
            "O número 4 é par!\n",
            "O número 5 é impar\n",
            "O número 6 é par!\n",
            "O número 7 é impar\n",
            "O número 8 é par!\n",
            "O número 9 é impar\n",
            "O número 10 é par!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UGDLPZdUNLb7",
        "outputId": "71aa51f0-20ec-4400-ce5b-dce6ec99f283"
      },
      "source": [
        "notas = [10, 8]\r\n",
        "\r\n",
        "soma = 0\r\n",
        "for nota in notas:\r\n",
        "  soma = soma + nota\r\n",
        "\r\n",
        "print('A soma vale', soma) \r\n",
        "\r\n",
        "media = soma / 2\r\n",
        "\r\n",
        "print('A média vale', media)"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A soma vale 18\n",
            "A média vale 9.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TiMC1lJ_OFbH",
        "outputId": "94b83b2d-ae3b-493b-da05-4edef3a09815"
      },
      "source": [
        "notas = [10, 8, 9, 7, 5]\r\n",
        "\r\n",
        "soma = 0\r\n",
        "for nota in notas:\r\n",
        "  soma = soma + nota\r\n",
        "\r\n",
        "print('A soma vale', soma) \r\n",
        "\r\n",
        "media = soma / 5\r\n",
        "\r\n",
        "print('A média vale', media)"
      ],
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A soma vale 39\n",
            "A média vale 7.8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XQbLj9TzOgkV",
        "outputId": "4706df8b-2329-4b65-b804-19220736f0e6"
      },
      "source": [
        "notas = [10, 8, 9]\r\n",
        "\r\n",
        "soma = 0\r\n",
        "for nota in notas:\r\n",
        "  soma = soma + nota\r\n",
        "\r\n",
        "print('A soma vale', soma) \r\n",
        "\r\n",
        "media = soma / 3\r\n",
        "\r\n",
        "print('A média vale', media)"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A soma vale 27\n",
            "A média vale 9.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UndcXYenOjYQ",
        "outputId": "dba4dea7-6c2a-4dc6-bc12-948e7c43715d"
      },
      "source": [
        "notas = [10, 8, 9, 7, 5]\r\n",
        "\r\n",
        "quantidade = len(notas)\r\n",
        "\r\n",
        "print('Quantidade de Notas:', quantidade)\r\n",
        "\r\n",
        "soma = 0\r\n",
        "for nota in notas:\r\n",
        "  soma = soma + nota\r\n",
        "\r\n",
        "print('A soma vale', soma) \r\n",
        "\r\n",
        "media = soma / quantidade\r\n",
        "\r\n",
        "print('A média vale', media)"
      ],
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Quantidade de Notas: 5\n",
            "A soma vale 39\n",
            "A média vale 7.8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CHN_g3D1OwTf",
        "outputId": "35cf93a6-ef01-4837-8284-eff2dff42ef7"
      },
      "source": [
        "notas = [10, 8, 9]\r\n",
        "\r\n",
        "quantidade = len(notas)\r\n",
        "print('Quantidade de Notas:', quantidade)\r\n",
        "\r\n",
        "soma = sum(notas)\r\n",
        "print('A soma vale', soma) \r\n",
        "\r\n",
        "media = soma / quantidade\r\n",
        "print('A média vale', media)"
      ],
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Quantidade de Notas: 3\n",
            "A soma vale 27\n",
            "A média vale 9.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P5Mv2xHDPFU3"
      },
      "source": [
        "notas = [10, 8, 9]\r\n",
        "\r\n",
        "quantidade = len(notas)\r\n",
        "soma = sum(notas)\r\n",
        "media = soma / quantidade\r\n",
        "\r\n",
        "\r\n",
        "print('A média vale', media)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TBnX_9tDRIdD",
        "outputId": "8a53175b-94b7-458f-9260-4e2dfb89f304"
      },
      "source": [
        "def calcular_media(notas):\r\n",
        "  quantidade = len(notas)\r\n",
        "  soma = sum(notas)\r\n",
        "  media = soma / quantidade\r\n",
        "  print('O aluno tirou', media)\r\n",
        "  return media\r\n",
        "\r\n",
        "def verificar_aprovacao(media):\r\n",
        "  if media >= 6:\r\n",
        "    print('Aluno Aprovado :)')\r\n",
        "  else:\r\n",
        "    print('Aluno Reprovado :(')\r\n",
        "\r\n",
        "jose = [1, 4, 6, 7]\r\n",
        "media = calcular_media(jose)\r\n",
        "verificar_aprovacao(media)"
      ],
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O aluno tirou 4.5\n",
            "Aluno Reprovado :(\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bTeVo3oiR8fh",
        "outputId": "f579a36f-4cf6-4c1b-e1a2-c7c02e19fc88"
      },
      "source": [
        "paulo = [10, 9, 8, 9]\r\n",
        "media = calcular_media(paulo)\r\n",
        "verificar_aprovacao(media)"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O aluno tirou 9.0\n",
            "Aluno Aprovado :)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zJ5YgYTjSWQ7",
        "outputId": "2526e4a4-5874-499c-a02c-8c4413b98d92"
      },
      "source": [
        "fabi = [6, 8, 4, 7]\r\n",
        "media = calcular_media(fabi)\r\n",
        "verificar_aprovacao(media)"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O aluno tirou 6.25\n",
            "Aluno Aprovado :)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f404k12bS-1W",
        "outputId": "a2e1965d-af20-4417-a104-d6f1abd359c7"
      },
      "source": [
        "def calcular_media(notas):\r\n",
        "  quantidade = len(notas)\r\n",
        "  soma = sum(notas)\r\n",
        "  media = soma / quantidade\r\n",
        "  print('O aluno tirou', media)\r\n",
        "  verificar_aprovacao(media)\r\n",
        "\r\n",
        "def verificar_aprovacao(media):\r\n",
        "  if media >= 6:\r\n",
        "    print('Aluno Aprovado :)')\r\n",
        "  else:\r\n",
        "    print('Aluno Reprovado :(')\r\n",
        "\r\n",
        "calcular_media([10, 9, 8, 7])\r\n"
      ],
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O aluno tirou 4.5\n",
            "Aluno Reprovado :(\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g9BDxQVtTsKh",
        "outputId": "439890f7-ef0d-4e57-e949-a25aa6bd8004"
      },
      "source": [
        "jose = [8, 7, 6, 7]\r\n",
        "calcular_media(jose)"
      ],
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O aluno tirou 7.0\n",
            "Aluno Aprovado :)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "odYzYCLXTvkA",
        "outputId": "57bfdca9-a814-4a21-a633-49eb28e2c750"
      },
      "source": [
        "def imc(peso, altura):\r\n",
        "  altura_quadrada = altura ** 2\r\n",
        "  meu_imc = peso / altura_quadrada\r\n",
        "  print(f'O meu imc é {meu_imc:.2f}')\r\n",
        "  return meu_imc\r\n",
        "\r\n",
        "meu_imc = imc(66, 1.75)"
      ],
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O meu imc é 21.55\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pEOXb61OUXUE",
        "outputId": "a70e49b6-b46a-4a8a-d1b1-8aa34b64719f"
      },
      "source": [
        "imc_katia = imc(70, 1.70)"
      ],
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O meu imc é 24.22\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ywKNm-wGVA_o"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}