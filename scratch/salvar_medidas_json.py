import json
import os

medidas = {
    "padrao_de_medida": {
        "definicao": "Bitola medida estritamente pela BORDA EXTERNA DA BASE (sapata de assentamento) de cada trilho, do extremo esquerdo ao extremo direito.",
        "regra_inviolavel": "Nao medir pelo centro do boleto, nao medir pelo bounding box do sprite, nao medir pela largura total de dormentes ou cavaletes.",
        "tolerancia_maxima_px": 1.0
    },
    "trilho_de_ligacao": {
        "asset": "res://assets/rails/estacao_trilho_v2.png",
        "canvas_nativo_px": {"w": 1008, "h": 810},
        "escala_no_jogo": 0.20,
        "posicao_no_mundo": {"x": -215.9, "y": 325.0},
        "extensao_vertical_mundo": {"y_topo": 244.0, "y_base": 406.0},
        "emenda_superior_tunel": {
            "y_textura_px": 20,
            "y_mundo_px": 248.0,
            "sapata_externa_esquerda_px": {"textura": 464.0, "mundo": -223.9},
            "sapata_externa_direita_px": {"textura": 796.0, "mundo": -157.5},
            "bitola_externa_px": {"textura": 332.0, "mundo": 66.4},
            "centro_par_x_px": {"textura": 630.0, "mundo": -190.7},
            "largura_cabeca_trilho_px": {"textura": 15.0, "mundo": 3.0},
            "passo_dormentes_px": {"textura": 120.0, "mundo": 24.0},
            "largura_dormente_px": {"textura": 485.0, "mundo": 97.0},
            "espessura_dormente_px": {"textura": 40.0, "mundo": 8.0}
        },
        "emenda_inferior_ponte": {
            "y_textura_px": 800,
            "y_mundo_px": 404.0,
            "sapata_externa_esquerda_px": {"textura": 387.0, "mundo": -239.3},
            "sapata_externa_direita_px": {"textura": 859.0, "mundo": -144.9},
            "bitola_externa_px": {"textura": 472.0, "mundo": 94.4},
            "centro_par_x_px": {"textura": 623.0, "mundo": -192.1},
            "largura_cabeca_trilho_px": {"textura": 7.0, "mundo": 1.4},
            "passo_dormentes_px": {"textura": 120.0, "mundo": 24.0},
            "largura_dormente_px": {"textura": 510.0, "mundo": 102.0},
            "espessura_dormente_px": {"textura": 42.0, "mundo": 8.4}
        },
        "variacao_angular_bitola_por_y": {
            "gradiente_bitola_px_por_px_mundo": 0.1795,
            "inclinacao_perspectiva_graus": 5.12
        }
    },
    "ponte_do_trilho": {
        "asset": "res://assets/rails/trilho_reto_vertical_v1.png",
        "cavalete_asset": "res://assets/rails/cavalete_alto_v1.png",
        "canvas_nativo_trilho_px": {"w": 745, "h": 982},
        "canvas_nativo_cavalete_px": {"w": 770, "h": 995},
        "escala_no_jogo": 0.25,
        "posicao_no_mundo": {"x": -188.0, "y": 499.75},
        "extensao_vertical_mundo": {"y_topo": 377.0, "y_base": 622.5},
        "emenda_superior_ligacao": {
            "y_textura_px": 116,
            "y_mundo_px": 406.0,
            "sapata_externa_esquerda_px": {"textura": 191.0, "mundo": -233.4},
            "sapata_externa_direita_px": {"textura": 520.0, "mundo": -151.1},
            "bitola_externa_px": {"textura": 329.0, "mundo": 82.3},
            "centro_par_x_px": {"textura": 355.5, "mundo": -192.25},
            "largura_cabeca_trilho_px": {"textura": 19.5, "mundo": 4.88},
            "passo_dormentes_px": {"textura": 46.6, "mundo": 11.65},
            "largura_dormente_px": {"textura": 485.0, "mundo": 121.25},
            "espessura_dormente_px": {"textura": 20.0, "mundo": 5.0}
        },
        "centro_travessia_canal": {
            "y_textura_px": 500,
            "y_mundo_px": 502.0,
            "sapata_externa_esquerda_px": {"textura": 136.0, "mundo": -247.1},
            "sapata_externa_direita_px": {"textura": 690.0, "mundo": -108.6},
            "bitola_externa_px": {"textura": 554.0, "mundo": 138.5},
            "centro_par_x_px": {"textura": 413.0, "mundo": -177.9},
            "largura_cabeca_trilho_px": {"textura": 7.5, "mundo": 1.88}
        },
        "ponta_sul_recebe_estacao": {
            "y_textura_px": 960,
            "y_mundo_px": 617.0,
            "sapata_externa_esquerda_px": {"textura": 103.0, "mundo": -255.4},
            "sapata_externa_direita_px": {"textura": 592.0, "mundo": -133.1},
            "bitola_externa_px": {"textura": 489.0, "mundo": 122.25},
            "centro_par_x_px": {"textura": 347.5, "mundo": -194.25},
            "largura_cabeca_trilho_px": {"textura": 7.5, "mundo": 1.88},
            "passo_dormentes_px": {"textura": 46.6, "mundo": 11.65},
            "largura_dormente_px": {"textura": 485.0, "mundo": 121.25},
            "espessura_dormente_px": {"textura": 20.0, "mundo": 5.0}
        },
        "variacao_angular_bitola_por_y": {
            "gradiente_bitola_px_por_px_mundo": 0.1893,
            "inclinacao_perspectiva_graus": 5.40
        }
    },
    "modulo_trilho_extensao_sul": {
        "tipo": "extensao_modular_aprovada_por_codigo",
        "modulo_base": "res://assets/rails/trilho_reto_vertical_v1.png",
        "escala_no_jogo": 0.25,
        "origem_conexao": {"x": -188.0, "y": 617.0},
        "destino_boca_estacao": {"x": -188.0, "y": 680.0},
        "comprimento_modulo_px": 63.0,
        "bitola_na_boca_estacao_px": {
            "textura_canvas_512x512": 320.0,
            "mundo_jogo_escala_0_25": 80.0
        }
    }
}

with open("medidas.json", "w", encoding="utf-8") as f:
    json.dump(medidas, f, indent=4, ensure_ascii=False)

print("Arquivo medidas.json gerado com sucesso!")
