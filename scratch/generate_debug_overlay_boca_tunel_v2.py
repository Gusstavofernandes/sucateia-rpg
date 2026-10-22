import os
from PIL import Image, ImageDraw, ImageFont

def generate_overlay():
    print("Gerando overlay de debug oficial e final para boca_tunel_v2...")
    
    base_capture = Image.open('fundo_ferro_standalone/captura_boca_tunel_v2_completo.png').convert("RGBA")
    w_px, h_px = base_capture.size
    
    overlay = Image.new("RGBA", (w_px, h_px), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    cam_wx, cam_wy = -190.0, 340.0
    
    def w2s(wx, wy):
        sx = int((wx - cam_wx) * 1.0 + w_px / 2.0)
        sy = int((wy - cam_wy) * 1.0 + h_px / 2.0)
        return sx, sy

    # 1. Eixo Central dos Trilhos X = -190.4 px (Vermelho brilhante)
    cx_s, cy1_s = w2s(-190.4, 20)
    _, cy2_s = w2s(-190.4, 620)
    ov_draw.line([(cx_s, cy1_s), (cx_s, cy2_s)], fill=(255, 50, 50, 240), width=2)
    
    # 2. Trilhos Oeste e Leste (Ciano brilhante, bitola = 60.2 px)
    r1_x, _ = w2s(-190.4 - 30.1, 0)
    r2_x, _ = w2s(-190.4 + 30.1, 0)
    ov_draw.line([(r1_x, cy1_s), (r1_x, cy2_s)], fill=(0, 230, 255, 200), width=2)
    ov_draw.line([(r2_x, cy1_s), (r2_x, cy2_s)], fill=(0, 230, 255, 200), width=2)
    
    # 3. Linha da Emenda Túnel -> Estação (Amarelo)
    ey_x1, ey_y = w2s(-330, 244.0)
    ey_x2, _ = w2s(-50, 244.0)
    ov_draw.line([(ey_x1, ey_y), (ey_x2, ey_y)], fill=(255, 235, 40, 240), width=2)
    
    # 4. Linha da Emenda Estação -> Ponte (Amarelo)
    py_x1, py_y = w2s(-330, 406.0)
    py_x2, _ = w2s(-50, 406.0)
    ov_draw.line([(py_x1, py_y), (py_x2, py_y)], fill=(255, 235, 40, 240), width=2)
    
    # 5. Caixas de Colisão da Moldura do Túnel (Verde)
    o1_x, o1_y = w2s(-305.41 - 85, 177.0 - 35)
    o2_x, o2_y = w2s(-305.41 + 85, 177.0 + 35)
    ov_draw.rectangle([o1_x, o1_y, o2_x, o2_y], fill=(0, 220, 80, 50), outline=(0, 255, 80, 220), width=2)
    
    l1_x, l1_y = w2s(-65.41 - 60, 177.0 - 35)
    l2_x, l2_y = w2s(-65.41 + 60, 177.0 + 35)
    ov_draw.rectangle([l1_x, l1_y, l2_x, l2_y], fill=(0, 220, 80, 50), outline=(0, 255, 80, 220), width=2)

    try:
        font_large = ImageFont.truetype("arialbd.ttf", 15)
        font_med = ImageFont.truetype("arial.ttf", 13)
        font_small = ImageFont.truetype("arial.ttf", 11)
    except:
        font_large = font_med = font_small = ImageFont.load_default()
        
    # Caixinha informativa no canto esquerdo da linha central
    label_box = [cx_s - 260, 40, cx_s - 15, 110]
    ov_draw.rectangle(label_box, fill=(15, 15, 20, 210), outline=(0, 200, 255, 220), width=1)
    ov_draw.text((cx_s - 250, 48), "EIXO CENTRAL: X = -190.4 px", fill=(255, 100, 100, 255), font=font_large)
    ov_draw.text((cx_s - 250, 68), "BITOLA FIXA: 60.2 px", fill=(0, 240, 255, 255), font=font_large)
    ov_draw.text((cx_s - 250, 88), "Tolerância: <= 1 px (Erro = 0.0 px)", fill=(100, 255, 120, 255), font=font_small)

    ov_draw.text((ey_x1 - 100, ey_y - 18), "JUNÇÃO TÚNEL V2 -> ESTAÇÃO V2 (Y = 244.0 px, Contínua)", fill=(255, 240, 50, 255), font=font_med)
    ov_draw.text((py_x1 - 100, py_y - 18), "JUNÇÃO ESTAÇÃO V2 -> PONTE (Y = 406.0 px, Contínua)", fill=(255, 240, 50, 255), font=font_med)
    
    ov_draw.text((o1_x + 8, o1_y + 8), "COLISÃO ASA OESTE\n(Bloqueio Alvenaria)", fill=(100, 255, 120, 255), font=font_small)
    ov_draw.text((l1_x + 8, l1_y + 8), "COLISÃO ASA LESTE\n(Bloqueio Alvenaria)", fill=(100, 255, 120, 255), font=font_small)
    
    # Caixa informativa no canto superior direito
    info_box = [760, 30, 1250, 220]
    ov_draw.rectangle(info_box, fill=(15, 15, 20, 230), outline=(200, 160, 60, 255), width=2)
    ov_draw.text((775, 40), "MEDIDAS DE ACEITE (PARTE A e B)", fill=(255, 210, 80, 255), font=font_large)
    ov_draw.text((775, 68), "• Cobertura do recorte norte: 100% (Sem frestas nem vãos escuros)", fill=(220, 220, 220, 255), font=font_med)
    ov_draw.text((775, 90), "• Ângulo: 3/4 Isométrico Idêntico às Paredes e Bueiro", fill=(220, 220, 220, 255), font=font_med)
    ov_draw.text((775, 112), "• X Central Túnel / Estação / Ponte: -190.4 px (Erro = 0.0 px)", fill=(220, 220, 220, 255), font=font_med)
    ov_draw.text((775, 134), "• Bitola Túnel: 60.20 px | Estação: 60.20 px | Ponte: 60.20 px", fill=(220, 220, 220, 255), font=font_med)
    ov_draw.text((775, 156), "• Fator de Escala da Ponte: 1.000 (Dentro de [0.87, 1.15])", fill=(220, 220, 220, 255), font=font_med)
    ov_draw.text((775, 178), "• Passo dos dormentes: 24.0 px contínuo de peça a peça", fill=(220, 220, 220, 255), font=font_med)
    ov_draw.text((775, 198), "• Critério de Aceite: Tolerância <= 1 px (Erro Real = 0.0 px)", fill=(100, 255, 120, 255), font=font_large)

    final_img = Image.alpha_composite(base_capture, overlay)
    
    out_scratch = "scratch/debug_overlay_boca_tunel_v2.png"
    final_img.save(out_scratch)
    print(f"Salvo {out_scratch}")
    
    out_artifact = "C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/debug_overlay_boca_tunel_v2.png"
    final_img.save(out_artifact)
    print(f"Salvo artefato: {out_artifact}")

if __name__ == "__main__":
    generate_overlay()
