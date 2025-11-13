"""Code syracuse
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """graphe"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(p: int) -> list:
    """retourne la suite de Syracuse de source n"""
    suite = [p]
    while p != 1:
        if p % 2 == 0:
            p = p // 2
        else:
            p = 3 * p + 1
        suite.append(p)

    return suite

def temps_de_vol(l: list) -> int:
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    return len(l) - 1

def temps_de_vol_en_altitude(l: list) -> int:
    """Retourne le temps de vol en altitude d'une suite de Syracuse"""
    u0 = l[0]
    tva = 0
    for u in l[1:]:
        if u > u0:
            tva += 1
        else:
            break
    return tva
def altitude_maximale(l: list) -> int:
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main():
    """FOonction où tout se teste"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
