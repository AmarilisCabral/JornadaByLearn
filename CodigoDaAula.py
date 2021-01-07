{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "PrimeiraAulaJornadaPythonFaixaPreta.ipynb",
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
        "id": "N-D88d3f4AHM"
      },
      "source": [
        "# Variável\r\n",
        "\r\n",
        "Um nome que se refere a um valor\r\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "M_Wmqd5S4JNf"
      },
      "source": [
        "# Variáveis \r\n",
        "\r\n",
        "Uma variável é um nome que se refere a um valor.\r\n",
        "\r\n",
        "# Atribuição\r\n",
        "\r\n",
        "Atribuição é passar um valor para a variável.\r\n",
        "\r\n",
        "Fazemos isso através do símbolo de igual (=)\r\n",
        "\r\n",
        "# Motivação do Uso\r\n",
        "\r\n",
        "São usadas para guardar valores e reutilizar mais tarde.\r\n",
        "\r\n",
        "Os valores podem ser alterados com o tempo.\r\n",
        "\r\n",
        "# Sintaxe\r\n",
        "\r\n",
        "variavel = valor\r\n",
        "\r\n",
        "variavel = novo_valor\r\n",
        "\r\n",
        "variavel2 = variavel1\r\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MyW9--PP3OWq"
      },
      "source": [
        "idade = 24 \r\n",
        "nome_completo = 'Felipe Cabrera'"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gMl1_2lo4Fh1",
        "outputId": "2f3a2150-2dd8-473b-d6b7-dd8f72fe2319"
      },
      "source": [
        "idade"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "24"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "UPpSKJ124uYN",
        "outputId": "94274179-a101-41a2-df23-811d63e901a8"
      },
      "source": [
        "nome_completo"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Felipe Cabrera'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MgXV59du4-xo"
      },
      "source": [
        "ano = 2021"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I4Cvvk3H5GVE"
      },
      "source": [
        "ano = 2022\r\n",
        "idade = 25"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6VU3PRpK5TNX",
        "outputId": "708bebca-eede-485b-95c8-9678626f4409"
      },
      "source": [
        "ano"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2022"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TCt4l4iO5Ty3",
        "outputId": "eda3f6eb-87d1-4724-909b-f8f3f4132aa8"
      },
      "source": [
        "idade"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "25"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mq_dr6Sy5VV2"
      },
      "source": [
        "numero = 10"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yv7JHlVK5hg1"
      },
      "source": [
        "numero_favorito = numero"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F-ljS0VP5i6X",
        "outputId": "662403ac-8dfb-4b4b-98f1-5b6f48bca2e9"
      },
      "source": [
        "numero_favorito"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6Pj-yJ5F5lwH"
      },
      "source": [
        "# Não pode ter espaço no nome da variável, precisa ser underline \r\n",
        "nome_completo = 'Felipe Cabrera'"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NA91bEaR58Ak"
      },
      "source": [
        "# Farei aqui meu comentário ou anotação\r\n",
        "codigo = 1"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "66sbZuRD6PPN"
      },
      "source": [
        "idade = 24\r\n",
        "nome = 'Felipe Cabrera'"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yY2yKHEf6qFh"
      },
      "source": [
        "# Tipos de Dados\r\n",
        "\r\n",
        "Basicamente um tipo de dado define o que é aquela variável:\r\n",
        "\r\n",
        "\r\n",
        "*   Números:\r\n",
        "  - Inteiros => **int**\r\n",
        "  - Decimais (com vírgula)  => **float**\r\n",
        "*   Texto (string) => **str**\r\n",
        "*   Booleanos (verdadeiro e falso) => **bool**\r\n",
        "\r\n",
        "Para se trabalhar com textos, devemos colocá-los entre aspas!\r\n",
        "\r\n",
        "Ex: \r\n",
        "- 23   => Número\r\n",
        "- '23' => Texto\r\n",
        "- Felipe Cabrera => Erro\r\n",
        "- 'Felipe Cabrera' => Certo\r\n",
        "\r\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Wbhhor7O6kjG"
      },
      "source": [
        "inteiro = 10\r\n",
        "decimal = 10.5\r\n",
        "\r\n",
        "texto = 'Felipe Cabrera'\r\n",
        "booleano = False"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "58GLG9YT7Sqg",
        "outputId": "456ac416-f757-47bb-ba74-f755011ac346"
      },
      "source": [
        "type(inteiro)"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SjjgZp-97Wo1",
        "outputId": "4420b92f-a62c-4d9b-ba7a-d5f8c775b788"
      },
      "source": [
        "type(decimal)"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MMsYwzoI7Y6o",
        "outputId": "5b9dbfa4-24b4-4415-b4c3-98f7759e3b14"
      },
      "source": [
        "type(texto)"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iVSFJ3eA7ajp",
        "outputId": "e5fb3735-96cc-4d3c-96bd-603baa189d13"
      },
      "source": [
        "type(booleano)"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "bool"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qis3nyDI7cgb",
        "outputId": "d9c9b481-1b11-4ed6-ba55-c9159dca3524"
      },
      "source": [
        "23 + 10"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "33"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "EhbujqEL7_0X",
        "outputId": "1711548e-7b4e-4324-d965-d76f8f504479"
      },
      "source": [
        "'23' + '10'"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'2310'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rvPsZGit8CqX"
      },
      "source": [
        "nome = 'Felipe Cabrera'"
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 171
        },
        "id": "nT3t0YS08a5O",
        "outputId": "82cddec3-75f4-4a57-dfde-15fcb74e6968"
      },
      "source": [
        "23 + '10'"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-30-59d822eef1e9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;36m23\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m'10'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ar0opua_85EH"
      },
      "source": [
        "letra = 'f'"
      ],
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wf5W0OuV9K4h",
        "outputId": "6bd7c9ec-088c-4721-a666-e6f82b877e2e"
      },
      "source": [
        "type(letra)"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jYAIDrgs9NCw",
        "outputId": "f7150491-50ed-4797-a7b0-57fa21be1a8b"
      },
      "source": [
        "type(gato)"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eionyUtq9Wbn"
      },
      "source": [
        "gato = 'Animal de estimação'"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YW-m5M8m9r1H"
      },
      "source": [
        "# Conversão de Tipos\r\n",
        "\r\n",
        "Inteiros => **int**\r\n",
        "\r\n",
        "Decimais (com vírgula) => **float**\r\n",
        "\r\n",
        "Texto (string) => **str**\r\n",
        "\r\n",
        "Booleano (verdadeiro e falso) => **bool**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nvcdAolV9ZAS"
      },
      "source": [
        "ano = 2021\r\n",
        "idade = '24'"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SDjepoLO9-Vq",
        "outputId": "bed6e7c8-ad71-4f4b-d89b-a8f9967b2103"
      },
      "source": [
        "type(ano)"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E71SwDSK-Av5",
        "outputId": "098dd7e7-6250-491f-ff7b-4ed662f94937"
      },
      "source": [
        "type(idade)"
      ],
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sUlncLLY-C1I"
      },
      "source": [
        "idade = int(idade)"
      ],
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AtobbAkC-JY8"
      },
      "source": [
        "ano = str(ano)"
      ],
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BvkzGTL_-Oq7"
      },
      "source": [
        "peso = 66"
      ],
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P10vKgCt-ULn",
        "outputId": "9620abfe-9f51-49e7-97de-253a4c9fce70"
      },
      "source": [
        "type(peso)"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IdmbRy-z-VcE"
      },
      "source": [
        "peso = float(peso)"
      ],
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zHrfWNpF-cO9"
      },
      "source": [
        "texto_10 = '10'\r\n",
        "numero_20 = 20"
      ],
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rwW0zNch-n8P"
      },
      "source": [
        "numero_10 = int(texto_10)\r\n",
        "texto_20 = str(numero_20)"
      ],
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S0A2U3Js-tNp",
        "outputId": "54834d0f-8d89-44b3-ce47-7338e116b5c4"
      },
      "source": [
        "type(numero_10)"
      ],
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CqxQaw9c-za2",
        "outputId": "77bce708-fa3e-47d8-bdd3-f781be0cfcf6"
      },
      "source": [
        "type(texto_20)"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eQp1sszC-1T5",
        "outputId": "b3ea8c78-3320-4976-c4d7-7ddcf4b2baa6"
      },
      "source": [
        "type(5.25)"
      ],
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k8VAzfkQ_XV-"
      },
      "source": [
        "# Operações Matemágicas\r\n",
        "\r\n",
        "Podemos executar várias operações matemáticas, como por exemplo:\r\n",
        "\r\n",
        "\r\n",
        "*   Soma => Símbolo de Mais (+)\r\n",
        "*   Subtração => Símbolo de Menos (-)\r\n",
        "*   Divisão => Símbolo de Dividir (/)\r\n",
        "*   Multiplicação => Símbolo de Multiplicar/Asterísco (*)\r\n",
        "\r\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "371_yOn4_H45"
      },
      "source": [
        "soma = 20 + 20"
      ],
      "execution_count": 52,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rer0UrJE_1V2",
        "outputId": "d359355d-51b0-48e6-8ec1-be6c06a73b9e"
      },
      "source": [
        "soma"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "40"
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
        "id": "o0FzLIIp_17I"
      },
      "source": [
        "subtracao = 40 - 20"
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
        "id": "VtjwB4RX_4kB",
        "outputId": "34990aee-58d9-42b3-d250-c770a0fa30f9"
      },
      "source": [
        "subtracao"
      ],
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pp2e5y3Y_50a"
      },
      "source": [
        "divisao = 10 / 5"
      ],
      "execution_count": 56,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JIvGcRxO_8wD",
        "outputId": "3314600e-18ca-4d40-8fc2-ddd2af178ed7"
      },
      "source": [
        "divisao"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8rbvRXXu_9_A"
      },
      "source": [
        "multiplicacao = 5 * 3"
      ],
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JJkWWQ1jABRr",
        "outputId": "4d4fdcc7-25d6-4995-c2cb-55aa9c54e7c5"
      },
      "source": [
        "multiplicacao"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "15"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 59
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IdOY7GluACT7",
        "outputId": "c36a6048-8d7f-4d29-9305-21ee7efeebdb"
      },
      "source": [
        "type(divisao)"
      ],
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 60
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kbpRs-MyAP8Y"
      },
      "source": [
        "divisao = 10 / 3"
      ],
      "execution_count": 61,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nu0ec4CPAXEn",
        "outputId": "98c4a163-5180-4fc0-b93d-169eeefe22cc"
      },
      "source": [
        "divisao"
      ],
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.3333333333333335"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QJ4lN2JPAXv4",
        "outputId": "3351e9a8-4d91-4f2c-c9c7-a672bd8be175"
      },
      "source": [
        "int(divisao)"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-IFaliuTAc-h"
      },
      "source": [
        "nome = 'Felipe'"
      ],
      "execution_count": 64,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "Gmf28-mfAnzV",
        "outputId": "3f44444a-36e2-431d-c7d8-331076adf765"
      },
      "source": [
        "nome "
      ],
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Felipe'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 66
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 171
        },
        "id": "XRZKLWh8AovF",
        "outputId": "a2ba6533-308e-45f6-cf2b-471056320d6b"
      },
      "source": [
        "divisao = 10 / 0"
      ],
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ZeroDivisionError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-67-991192aa39f1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdivisao\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m10\u001b[0m \u001b[0;34m/\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LTvBmVonBQeF"
      },
      "source": [
        "# Métodos de Entrada\r\n",
        "\r\n",
        "São formas de enviar dados para o Python.\r\n",
        "\r\n",
        "Ou seja, nós (usuários) entramos com dados para ser processado pelo programa em Python.\r\n",
        "\r\n",
        "Ex: Perguntar o nome e a idade do usuário.\r\n",
        "\r\n",
        "Para isso, usamos o input e informamos uma mensagem dentro dos parânteses.\r\n",
        "\r\n",
        "Além disso, o input sempre retorna uma string."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rVdx2KHbBGVr",
        "outputId": "c8f851f1-d450-40b9-bba0-36e16970321b"
      },
      "source": [
        "nome = input('Qual o seu nome? ')\r\n",
        "idade = int(input('Qual a sua idade? '))"
      ],
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Qual o seu nome? Felipe\n",
            "Qual a sua idade? 24\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "9CEWncZOB-2l",
        "outputId": "134dfa38-20c7-4f8f-a2aa-b7dc621c7e82"
      },
      "source": [
        "nome"
      ],
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Felipe'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 73
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "01tKyJjWCEb3",
        "outputId": "bc366f4d-371a-470f-faed-2494b0d8f590"
      },
      "source": [
        "idade"
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "24"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XM-rfur4CFhv"
      },
      "source": [
        "idade = idade + 1"
      ],
      "execution_count": 75,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "is0I7wBzCNDK",
        "outputId": "0c620c0c-74fe-4ee3-8153-e37ca70f45c1"
      },
      "source": [
        "idade"
      ],
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "25"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 76
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KXrNqrPUCrNJ"
      },
      "source": [
        "numero_favorito = 10"
      ],
      "execution_count": 77,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DyEM8vsMC5uT"
      },
      "source": [
        "numero_favorito = 5"
      ],
      "execution_count": 78,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kwvv4jXRC7jO"
      },
      "source": [
        "numero_favorito = 2"
      ],
      "execution_count": 79,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dXtkz5XvC9My"
      },
      "source": [
        "resto_divisao = 10 % 3"
      ],
      "execution_count": 83,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bZOj7PgPDLRN",
        "outputId": "2abc3962-6688-4ef6-f06a-a1d63c473a8c"
      },
      "source": [
        "resto_divisao"
      ],
      "execution_count": 84,
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
          "execution_count": 84
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nHje_t9ODOAT"
      },
      "source": [
        "disivao_inteiro = 10 // 3"
      ],
      "execution_count": 85,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v2h3Xd0sDe68",
        "outputId": "597a8019-de46-4cd9-aa49-7992a40fdaa0"
      },
      "source": [
        "disivao_inteiro"
      ],
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 86
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z-s_EVtLDgId",
        "outputId": "af7203db-9ccf-4ec1-ac7b-1d626da963ad"
      },
      "source": [
        "# Calculadora da ByLearn\r\n",
        "\r\n",
        "# Entrada dos números\r\n",
        "primeiro_numero = float(input('Digite o primeiro número: '))\r\n",
        "segundo_numero = float(input('Digite o segundo número: '))\r\n",
        "\r\n",
        "# Operações Matemáticas\r\n",
        "soma = primeiro_numero + segundo_numero\r\n",
        "subtracao = primeiro_numero - segundo_numero\r\n",
        "multiplicacao = primeiro_numero * segundo_numero\r\n",
        "divisao = primeiro_numero / segundo_numero"
      ],
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Digite o primeiro número: 25\n",
            "Digite o segundo número: 5\n"
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
        "id": "nX94cJTOEXAq",
        "outputId": "261fdf41-b871-4c8d-a3b4-784eae201727"
      },
      "source": [
        "soma"
      ],
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "30.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 88
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MOwUcqnfEbrJ",
        "outputId": "d3af1dde-66ed-4538-d56f-f583f6b90247"
      },
      "source": [
        "subtracao"
      ],
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 89
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vav7SVNcEd_d",
        "outputId": "7eca544e-bf09-4865-9264-7a444a4bd79d"
      },
      "source": [
        "multiplicacao"
      ],
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "125.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 90
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JjyoOb6eEgDE",
        "outputId": "55b33725-9201-4e8e-ab17-d8e95f3712e3"
      },
      "source": [
        "divisao"
      ],
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 91
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hrb3L_qrEuL7"
      },
      "source": [
        "# Métodos de Saída\r\n",
        "\r\n",
        "São formas do Python mostrar os dados aos usuários\r\n",
        "\r\n",
        "Usamos a função print() e enviamos a mensagem/variavel que queremos mostrar ao usuário"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uPQwoT_xEiEU",
        "outputId": "67ecf98c-c574-4c01-c52c-e1937987976e"
      },
      "source": [
        "print('O resultado é:')"
      ],
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O resultado é:\n"
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
        "id": "IAj0IAqSE7SX",
        "outputId": "1d793365-f48c-42ad-f18e-11593fecc55f"
      },
      "source": [
        "print(divisao)"
      ],
      "execution_count": 93,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "5.0\n"
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
        "id": "PtneHcFxE9d-",
        "outputId": "37d73da3-b0b2-4ebc-eb80-33174dc8ad10"
      },
      "source": [
        "# Concatenar Strings => Juntar Strings\r\n",
        "print('O resultado é', divisao)"
      ],
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O resultado é 5.0\n"
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
        "id": "nOoN2nN5FGT7",
        "outputId": "c64170fb-6161-401b-b005-31c685ec3276"
      },
      "source": [
        "# Calculadora da ByLearn\r\n",
        "\r\n",
        "# Entrada dos números\r\n",
        "primeiro_numero = float(input('Digite o primeiro número: '))\r\n",
        "segundo_numero = float(input('Digite o segundo número: '))\r\n",
        "\r\n",
        "# Operações Matemáticas\r\n",
        "soma = primeiro_numero + segundo_numero\r\n",
        "subtracao = primeiro_numero - segundo_numero\r\n",
        "multiplicacao = primeiro_numero * segundo_numero\r\n",
        "divisao = primeiro_numero / segundo_numero\r\n",
        "\r\n",
        "# Saída dos cálculos\r\n",
        "print('A soma é', soma)\r\n",
        "print('A subtração é', subtracao)\r\n",
        "print('A multiplicação é', multiplicacao)\r\n",
        "print('A divisão é', divisao)"
      ],
      "execution_count": 95,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Digite o primeiro número: 25\n",
            "Digite o segundo número: 5\n",
            "A soma é 30.0\n",
            "A subtração é 20.0\n",
            "A multiplicação é 125.0\n",
            "A divisão é 5.0\n"
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
        "id": "l4m729qHFW6g",
        "outputId": "2e42b617-8f81-45e4-a570-d90bc7853b5f"
      },
      "source": [
        "# A soma entre [25] e [5] é [30]\r\n",
        "print('A soma entre', primeiro_numero, 'e', segundo_numero, 'é', soma)"
      ],
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A soma entre 25.0 e 5.0 é 30.0\n"
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
        "id": "9ahPSEPSFuZm",
        "outputId": "892636cd-26ff-4f56-bf46-cb86403573af"
      },
      "source": [
        "print(f'A soma entre {primeiro_numero} e {segundo_numero} é {soma}!')"
      ],
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A soma entre 25.0 e 5.0 é 30.0!\n"
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
        "id": "0GaIA3YEGJzW",
        "outputId": "389db575-e19a-4add-f609-c39d4ea515fc"
      },
      "source": [
        "# Calculadora da ByLearn\r\n",
        "\r\n",
        "# Entrada dos números\r\n",
        "primeiro_numero = float(input('Digite o primeiro número: '))\r\n",
        "segundo_numero = float(input('Digite o segundo número: '))\r\n",
        "\r\n",
        "# Operações Matemáticas\r\n",
        "soma = primeiro_numero + segundo_numero\r\n",
        "subtracao = primeiro_numero - segundo_numero\r\n",
        "multiplicacao = primeiro_numero * segundo_numero\r\n",
        "divisao = primeiro_numero / segundo_numero\r\n",
        "\r\n",
        "# Saída dos cálculos\r\n",
        "print(f'A soma entre {primeiro_numero} e {segundo_numero} é {soma}!')\r\n",
        "print(f'A subtração entre {primeiro_numero} e {segundo_numero} é {subtracao}!')\r\n",
        "print(f'A multiplicação entre {primeiro_numero} e {segundo_numero} é {multiplicacao}!')\r\n",
        "print(f'A divisão entre {primeiro_numero} e {segundo_numero} é {divisao}!')"
      ],
      "execution_count": 98,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Digite o primeiro número: 25\n",
            "Digite o segundo número: 5\n",
            "A soma entre 25.0 e 5.0 é 30.0!\n",
            "A subtração entre 25.0 e 5.0 é 20.0!\n",
            "A multiplicação entre 25.0 e 5.0 é 125.0!\n",
            "A divisão entre 25.0 e 5.0 é 5.0!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TqGZ9jZTI9wf"
      },
      "source": [
        "# Listas\r\n",
        "\r\n",
        "Métodos de trabalhar com sequências\r\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S-GhCy1II_g6"
      },
      "source": [
        "animais = ['Cachorro', 'Gato', 'Coelho', 'Furão', 'Hamster']\r\n",
        "# Posições:   1           2       3         4         5\r\n",
        "# Índices:    0           1       2         3         4"
      ],
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "zlzwXNfdJSM3",
        "outputId": "c2f4d2d1-2c41-495f-94e1-269403e052db"
      },
      "source": [
        "animais[1]"
      ],
      "execution_count": 102,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Gato'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 102
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "AeKiIcVqJS-v",
        "outputId": "3cbdeca9-16a0-4877-aa55-d145239ea469"
      },
      "source": [
        "animais[3]"
      ],
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Furão'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WiNOWAPqJW3s",
        "outputId": "d219e050-7f52-4779-dd61-37a654c5263e"
      },
      "source": [
        "print('A Shura é uma', animais[3])\r\n",
        "print('O Obi-Wan é um', animais[1])\r\n",
        "print('O Dwight é um', animais[4])\r\n"
      ],
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A Shura é uma Furão\n",
            "O Obi-Wan é um Gato\n",
            "O Dwight é um Hamster\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V3ZATEo7JoHi"
      },
      "source": [
        "dwigth = animais[4]\r\n",
        "obiwan = animais[1]\r\n",
        "shura = animais[3]"
      ],
      "execution_count": 107,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MoG98LLHJwgC",
        "outputId": "fe7856d8-5f8a-49ed-ba27-041a29e94968"
      },
      "source": [
        "print('A Shura é uma', shura)\r\n",
        "print('O Obi-Wan é um', obiwan)\r\n",
        "print('O Dwight é um', dwigth)\r\n"
      ],
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A Shura é uma Furão\n",
            "O Obi-Wan é um Gato\n",
            "O Dwight é um Hamster\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WQfUckUKJ3yu"
      },
      "source": [
        "numeros = [1, 3, 5, 7, 9]\r\n",
        "\r\n",
        "cinco = numeros[2]\r\n",
        "nove = numeros[4]"
      ],
      "execution_count": 109,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tpJctOF7KF4h",
        "outputId": "fd1fa343-abc5-4d1a-c440-9800a8f8be1e"
      },
      "source": [
        "cinco"
      ],
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 110
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZIqHUuspKG6M",
        "outputId": "9cacb42e-fe8e-4fb6-b393-11cff84e0c08"
      },
      "source": [
        "nove"
      ],
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 111
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qT6cvr5UKHxW"
      },
      "source": [
        "lista_de_lista = [   ['Doctor',2]    ,   ['Felipe',4]   ,   ['Shura',6]    ]"
      ],
      "execution_count": 117,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MSqMY77vKWEV"
      },
      "source": [
        "primeira_sublista = lista_de_lista[0]"
      ],
      "execution_count": 118,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q7EptsnJKYLF",
        "outputId": "2cca1c31-d4aa-45a6-ef84-0820bd372e1f"
      },
      "source": [
        "primeira_sublista"
      ],
      "execution_count": 119,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Doctor', 2]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 119
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "j-nJD7HZKZmS"
      },
      "source": [
        "primeiro_dado = primeira_sublista[0]"
      ],
      "execution_count": 120,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "oZ9CVI0yKeWH",
        "outputId": "0016a5e0-9743-49f3-9f66-4f2408979f91"
      },
      "source": [
        "primeiro_dado"
      ],
      "execution_count": 121,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Doctor'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X6DC0-O6KflH"
      },
      "source": [
        "segundo_dado = lista_de_lista[0][1]"
      ],
      "execution_count": 122,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5amlgjljK0I5",
        "outputId": "7ed78f79-8174-415c-ebea-0100d58d303f"
      },
      "source": [
        "segundo_dado"
      ],
      "execution_count": 123,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 123
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7s3E5biYK1DH"
      },
      "source": [
        "lista_vazia = []"
      ],
      "execution_count": 124,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8VrBedpTLRxa"
      },
      "source": [
        "lista_vazia.append('Felipe')"
      ],
      "execution_count": 125,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zGUIYHzULXK5"
      },
      "source": [
        "lista_vazia.append(24)"
      ],
      "execution_count": 126,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1PZgZPtrXJT7"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y6edh0RmLZgW"
      },
      "source": [
        "lista_vazia.append(11)"
      ],
      "execution_count": 127,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v3JpTC8sLax9"
      },
      "source": [
        "lista_vazia.append('ByLearn')"
      ],
      "execution_count": 128,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oMcCXB3SLckN",
        "outputId": "433f00c5-a391-450b-cdb7-b69f89701e63"
      },
      "source": [
        "lista_vazia"
      ],
      "execution_count": 129,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Felipe', 24, 11, 'ByLearn']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 129
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "43cdThU9LdvB",
        "outputId": "9a6b475c-ade0-4cc6-c361-ec29a2b21a4d"
      },
      "source": [
        "print(f'O {lista_vazia[0]} tem {lista_vazia[1]} anos, possui {lista_vazia[2]} gatos e é professor na {lista_vazia[3]}')"
      ],
      "execution_count": 130,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "O Felipe tem 24 anos, possui 11 gatos e é professor na ByLearn\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lvBtaqexLp-I"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}