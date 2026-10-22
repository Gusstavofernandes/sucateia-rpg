Codex, trate esta resposta como **auditoria de direção**, não como brainstorm. O estado atual de Forjas Rasas ainda está abaixo do padrão que queremos. Há boas decisões, mas você está aceitando cedo demais soluções “funcionais” que ainda parecem montadas por módulos. Corrija isso antes de expandir.

**Problemas reais observáveis nas capturas:**

- A transição Mercado → Forjas ainda acontece mais pelos prédios do que pelo ambiente. O chão muda pouco e tarde demais. Isso deixa a sensação de que você “colocou assets industriais” sobre o mesmo bairro.
- Os vazios das Forjas não estão lendo como pátios produtivos; estão lendo como espaço não preenchido. Isso é um problema de composição e função, não de quantidade de props.
- O landmark industrial atual é bom, mas ainda não domina a silhueta. No panorama ele vira “mais uma construção quente” e não “o coração das Forjas”.
- Há pouca costura entre os edifícios industriais. Eles parecem vizinhos, não partes de um sistema.
- A borda externa das Forjas ainda tem leitura de “aba anexada” ao mapa. Precisa parecer continuidade regional, não expansão retangular.
- A distribuição de luz ainda está tímida. Forjas precisa contaminar mais o entorno com calor, fuligem e reflexo industrial.
- O setor ainda não comunica suficientemente **produção em escala**. Ele comunica “oficinas e forjas”, mas não “distrito produtivo”.

**O que deve ser preservado:**
- posição leste/nordeste;
- integração geral com Mercado;
- linguagem dos novos prédios;
- contraste âmbar/laranja;
- uso de tubos e metal remendado;
- ausência de corte seco entre distritos.

Agora, os prompts de assets enviados antes estão **bons demais no abstrato e fracos demais no encaixe real**. Eles pedem assets bonitos, mas não exigem suficientemente:
- escala compatível com os sprites atuais;
- largura e altura relativas;
- direção exata de luz;
- margem para recorte;
- conexão física com assets existentes;
- modularidade por encaixe;
- sombra de contato;
- leitura em zoom de gameplay;
- consistência com a câmera atual;
- variações de dano/uso;
- integração com terreno já existente.

A partir de agora, todo prompt de asset para Forjas Rasas deve incluir este bloco obrigatório:

```text
PRODUCTION CONSTRAINTS:
- match the exact elevated 3/4 top-down camera of the current game;
- match the scale of the existing Ferrugem Baixa buildings;
- readable at gameplay zoom, not only as concept art;
- no dramatic cinematic perspective;
- lighting from the same general direction as current map assets;
- include believable ground contact and base shadow;
- preserve clean silhouette for sprite extraction;
- avoid oversized roof overhangs that obscure walkable space;
- avoid frontal perspective;
- no isolated decorative pipes without visible connection logic;
- materials must match current Ferrugem Baixa: dark stone, rusted iron, copper, patched wood, soot;
- use cyan arcane light only as a secondary accent;
- orange forge light is primary in Forjas Rasas;
- asset must visually belong beside the current Mercado/Forjas transition;
- output should be usable as an in-game sprite, not only as key art.
```

E para modular assets, acrescente:

```text
MODULARITY:
- provide clear connection points;
- pipe ends, wall joins and platform edges must align cleanly;
- avoid asymmetry that prevents reuse unless the asset is a landmark;
- produce variants that differ in function, not just color;
- every module must imply a believable industrial purpose.
```

**Correções prioritárias, nesta ordem:**

1. **Terreno de transição**
   Não adicione mais prédios antes de resolver isso. Faça uma faixa clara de 15–30% do setor onde pedra urbana vira pedra escurecida, metal remendado, fuligem, escória e piso queimado.

2. **Pátios funcionais**
   Pegue os vazios existentes e transforme cada um em UMA função:
   - carvão;
   - minério;
   - escória;
   - resfriamento;
   - manutenção.
   
   Não espalhe props aleatórios. Agrupe por função.

3. **Landmark**
   A forja central precisa ganhar uma silhueta inequívoca. Não substitua. Amplie com:
   - uma chaminé principal alta;
   - dutos grossos;
   - plataforma de manutenção;
   - exaustão visível;
   - uma base mais marcada.
   
   Teste no panorama. Se não for identificável de imediato, ainda está fraco.

4. **Costura industrial**
   Conecte os prédios:
   - tubos curtos;
   - passarelas;
   - canaletas;
   - suportes;
   - áreas de carga.
   
   O jogador deve perceber que tudo faz parte de uma cadeia produtiva.

5. **Borda externa**
   Pare de desenhar limite de setor como “fim de mapa”. Faça:
   - estruturas continuando;
   - tubos saindo;
   - depósitos periféricos;
   - contenções;
   - plataformas.
   
   A Forja deve parecer continuar além da câmera.

**Assets que realmente faltam agora:**
- chaminé/torre de exaustão modular para o landmark;
- pátio de carvão/minério/escória em clusters funcionais;
- oficina híbrida Mercado→Forja;
- conectores curtos de tubo/passarela;
- decals de fuligem/escória/chão queimado;
- suportes e braçadeiras visíveis para tubos;
- um módulo de resfriamento com tanque/canaleta;
- um módulo de carga com carrinho/guincho/lingotes.

Use este prompt melhorado para o landmark:

```text
Create a production-ready add-on module for the existing central furnace landmark in Forjas Rasas.

ASSET:
A tall goblin exhaust tower and heavy industrial chimney assembly that attaches to an existing forge structure.

VISUAL PURPOSE:
Make the central forge readable as the dominant landmark of Forjas Rasas from the Mercado at long distance.

DESIGN:
- one dominant vertical chimney;
- two smaller auxiliary vents;
- heavy rusted iron frame;
- dark soot-blackened stone base;
- copper pressure pipes;
- riveted repair plates;
- maintenance platform;
- ladder;
- structural braces;
- ash vents;
- subtle cyan arcane gauge accents;
- strong orange heat glow only near the lower furnace connection.

FUNCTIONAL LOGIC:
- visible intake/outflow points;
- believable exhaust path;
- clear attachment points to an existing furnace;
- no decorative floating pipes;
- every pipe must terminate logically.

PRODUCTION CONSTRAINTS:
- exact elevated 3/4 top-down camera of current game;
- same scale as current Ferrugem Baixa buildings;
- readable at gameplay zoom;
- same lighting direction as current map;
- clean silhouette;
- transparent or clean extraction background;
- no text;
- no characters;
- no cinematic perspective;
- no generic steampunk styling.

GOAL:
This should look like the unmistakable industrial heart of Forjas Rasas, not just another building.
```

Para os pátios:

```text
Create a modular set of functional goblin industrial yard clusters for Forjas Rasas.

Provide 4 distinct clusters:
1. coal storage yard;
2. ore and scrap intake yard;
3. slag disposal yard;
4. cooling and maintenance yard.

Each cluster must read immediately by function.

Include:
- grouped props;
- floor wear;
- small support structures;
- carts;
- bins;
- tool racks;
- hoists;
- ash or slag;
- cooling trough where relevant.

Do not scatter props randomly.

PRODUCTION CONSTRAINTS:
- exact elevated 3/4 top-down camera;
- same scale as current map;
- compatible lighting;
- strong ground contact;
- transparent background;
- readable at gameplay zoom;
- modular and reusable;
- no characters;
- no text.
```

E para a transição Mercado → Forjas:

```text
Create a transition workshop asset that visually bridges Mercado dos Restos and Forjas Rasas.

It must combine:
- remnant market awning;
- timber storefront;
- trade counter;
with:
- small furnace;
- soot;
- metal plating;
- pipework;
- tool rack;
- scrap bin;
- copper vent.

It should look like a commercial stall that evolved into a metalworking shop.

PRODUCTION CONSTRAINTS:
- exact current game camera;
- same building scale;
- same lighting direction;
- gameplay-readable silhouette;
- integrated base shadow;
- no exaggerated roof;
- no generic medieval blacksmith;
- no full heavy industry look;
- must sit naturally at the border between current Market and Forge assets.
```

**Critério de aprovação para Forjas Rasas:**

Eu só consideraria o setor aprovado quando, em um panorama sem labels, for possível identificar:
- onde o Mercado termina e Forjas começa;
- qual é o landmark principal;
- pelo menos 3 zonas produtivas com função legível;
- continuidade física entre os prédios;
- ausência de “grandes vazios neutros”;
- ausência de sensação de mapa separado.

Não expanda o setor antes disso. Faça essas correções primeiro e depois mande nova captura geral + uma captura da transição.