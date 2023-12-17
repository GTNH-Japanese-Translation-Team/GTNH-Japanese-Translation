import json

to_replace = {
    'Block of %material': '%materialブロック',
    '1x %material Cable': '1倍%materialケーブル',
    '2x %material Cable': '2倍%materialケーブル',
    '4x %material Cable': '4倍%materialケーブル',
    '8x %material Cable': '8倍%materialケーブル',
    '12x %material Cable': '12倍%materialケーブル',
    '16x %material Cable': '16倍%materialケーブル',
    '%material Frame Box': '%material製の骨組み',
    'Huge %material Item Pipe': '極太の%material製アイテムパイプ',
    'Large %material Item Pipe': '太い%material製アイテムパイプ',
    '%material Item Pipe': '%material製アイテムパイプ',
    'Small %material Item Pipe': '細い%material製アイテムパイプ',
    'Tiny %material Item Pipe': '極細の%material製アイテムパイプ',
    'Huge Restrictive %material Item Pipe': '極太の%material製制限アイテム',
    'Large Restrictive %material Item Pipe': '太い%material製制限アイテムパイプ',
    'Restrictive %material Item Pipe': '%material製制限アイテムパイプ',
    'Small Restrictive %material Item Pipe': '細い%material製制限アイテムパイプ',
    'Tiny Restrictive %material Item Pipe': '極細の%material製制限アイテムパイプ',
    'Huge %material Fluid Pipe': '極太の%material製液体パイプ',
    'Large %material Fluid Pipe': '太い%material製液体パイプ',
    '%material Fluid Pipe': '%material製液体パイプ',
    'Small %material Fluid Pipe': '細い%material製液体パイプ',
    'Tiny %material Fluid Pipe': '極細の%material製液体パイプ',
    'Quadruple %material Fluid Pipe': '%material製四重液体パイプ',
    'Nonuple %material Fluid Pipe': '%material製九重液体パイプ',
    '1x %material Wire': '1倍%materialワイヤー',
    '2x %material Wire': '2倍%materialワイヤー',
    '4x %material Wire': '4倍%materialワイヤー',
    '8x %material Wire': '8倍%materialワイヤー',
    '12x %material Wire': '12倍%materialワイヤー',
    '16x %material Wire': '16倍%materialワイヤー',
    '%material Ore': '%material鉱石',
    '%material Infused Stone': '%materialの染み込んだ石', # Thaumcraft
    'Small %material Ore': '小さな%material鉱石',
    'Small %material': '小さな%material', # mineral
    'Small %material Infused Stone': '%materialの染み込んだ小さな石', # Thaumcraft
    # dustTiny
    'Tiny Pile of %material Dust': 'とても小さな%materialの粉',
    'Tiny Pile of %material': 'とても小さな%material', # mineral
    'Tiny Pile of %material Pulp': 'とても小さな%materialのパルプ', # polymer
    'Tiny Pile of %material Powder': 'とても小さな%materialの粉', # food
    'Tiny Pile of %material Crystal Powder': 'とても小さな%materialの結晶の粉', # Thaumcraft
    # dustSmall
    'Small Pile of %material Dust': '小さな%materialの粉',
    'Small Pile of %material': '小さな%material', # mineral
    'Small Pile of %material Pulp': '小さな%materialのパルプ', # polymer
    'Small Pile of %material Powder': '小さな%materialの粉', # food
    'Small Pile of %material Crystal Powder': '小さな%materialの結晶の粉', # Thaumcraft
    # dust
    '%material Dust': '%materialの粉',
    '%material Pulp': '%materialのパルプ', # polymer
    '%material Powder': '%materialの粉', # food
    '%material Crystal Powder': '%materialの結晶の粉', # Thaumcraft
    # dustImpure
    'Impure Pile of %material Dust': '汚れた%materialの粉',
    'Impure Pile of %material': '汚れた%material', # mineral
    'Impure Pile of %material Powder': '汚れた%materialの粉', # food
    'Impure Pile of %material Crystal Powder': '汚れた%materialの結晶の粉', # Thaumcraft
    # dustPure
    'Purified Pile of %material Dust': 'ほぼ綺麗な%materialの粉',
    'Purified Pile of %material': 'ほぼ綺麗な%material', # mineral
    'Purified Pile of %material Powder': 'ほぼ綺麗な%materialの粉', # food
    'Purified Pile of %material Crystal Powder': 'ほぼ綺麗な%materialの結晶の粉', # Thaumcraft
    # crushed
    'Crushed %material Ore': '粉砕した%material鉱石',
    'Ground %material': '粉砕した%material', # mineral
    'Crushed %material Crystals': '粉砕した%materialの結晶', # Thaumcraft
    # crushedPurified
    'Purified %material Ore': '洗浄した%material鉱石',
    'Purified %material': '洗浄した%material', # mineral
    'Purified %material Crystals': '洗浄した%materialの結晶', # Thaumcraft
    # crushedCentrifuged
    'Centrifuged %material Ore': '遠心分離した%material鉱石',
    'Centrifuged %material': '遠心分離した%material', # mineral
    'Centrifuged %material Crystals': '遠心分離した%materialの結晶', # Thaumcraft
    # gem
    '%material': '%material',
    'Shard of %material': '%materialの結晶片', # Thaumcraft
    '%material Crystal': '%materialの結晶', # glass-like
    # nugget
    '%material Nugget': '%materialナゲット',
    '%material Chip': '%materialのチップ', # polymer
    # ingot
    '%material Ingot': '%materialインゴット',
    '%material Bar': '%materialバー', # polymer
    # ingotHot
    'Hot %material Ingot': '熱い%materialインゴット',
    # ingotDouble
    'Double %material Ingot': '二重%materialインゴット',
    'Double %material Bar': '二重%materialバー', # polymer
    'Double %material': '二重%material', # Steeleaf
    # ingotTriple
    'Triple %material Ingot': '三重%materialインゴット',
    'Triple %material Bar': '三重%materialバー', # polymer
    'Triple %material': '三重%material', # Steeleaf
    # ingotQuadruple
    'Quadruple %material Ingot': '四重%materialインゴット',
    'Quadruple %material Bar': '四重%materialバー', # polymer
    'Quadruple %material': '四重%material', # Steeleaf
    # ingotQuintuple
    'Quintuple %material Ingot': '五重%materialインゴット',
    'Quintuple %material Bar': '五重%materialバー', # polymer
    'Quintuple %material': '五重%material', # Steeleaf
    # plate
    '%material Plate': '%materialプレート',
    '%material Sheet': '%materialシート', # polymer
    '%material Crystal Plate': '%materialの結晶のプレート', # Thaumcraft
    '%material Plank': '%materialの板', # wood-like
    '%material Pane': '%material板', # glass-like
    # plateDouble
    'Double %material Plate': '二重%materialプレート',
    'Double %material Sheet': '二重%materialシート', # polymer
    # plateTriple
    'Triple %material Plate': '三重%materialプレート',
    'Triple %material Sheet': '三重%materialシート', # polymer
    # plateQuadruple
    'Quadruple %material Plate': '四重%materialプレート',
    'Quadruple %material Sheet': '四重%materialシート', # polymer
    # plateQuintuple
    'Quintuple %material Plate': '五重%materialプレート',
    'Quintuple %material Sheet': '五重%materialシート', # polymer
    # plateDense
    'Dense %material Plate': '高密度な%materialプレート',
    'Dense %material Sheet': '高密度な%materialシート', # polymer
    # stick
    '%material Rod': '%materialの棒',
    '%material Stick': '%materialの棒', # wood-like
    # lens
    '%material Lens': '%materialのレンズ',
    # round
    '%material Round': '%materialのボール',
    # bolt
    '%material Bolt': '%materialのボルト',
    'Short %material Stick': '短い%materialの棒', # wood-like
    # screw
    '%material Screw': '%materialのスクリュー',
    # ring
    '%material Ring': '%materialのリング',
    # foil
    '%material Foil': '%materialのホイル',
    'Thin %material Sheet': '薄い%materialシート', # polymer
    # cell
    '%material Cell': '%materialのセル',
    # cellPlasma
    '%material Plasma Cell': '%materialプラズマのセル',
    # toolHeadSword
    '%material Sword Blade': '%material製剣刃',
    # toolHeadPickaxe
    '%material Pickaxe Head': '%material製ツルハシヘッド',
    # toolHeadShovel
    '%material Shovel Head': '%material製シャベル刃',
    # toolHeadAxe
    '%material Axe Head': '%material製斧刃',
    # toolHeadHoe
    '%material Hoe Head': '%material製クワ刃',
    # toolHeadHammer
    '%material Hammer Head': '%material製ハンマーヘッド',
    # toolHeadFile
    '%material File Head': '%material製ヤスリ刃',
    # toolHeadSaw
    '%material Saw Blade': '%material製ノコギリ刃',
    # toolHeadDrill
    '%material Drill Tip': '%material製ドリル刃',
    # toolHeadChainsaw
    '%material Chainsaw Tip': '%material製チェーンソー刃',
    # toolHeadWrench
    '%material Wrench Tip': '%material製レンチヘッド',
    # toolHeadUniversalSpade
    '%material Universal Spade Head': '%material製多目的シャベル刃',
    # toolHeadSense
    '%material Sense Blade': '%material製鎌刃',
    # toolHeadPlow
    '%material Plow Head': '%material製すき刃',
    # toolHeadArrow
    '%material Arrow Head': '%material製矢じり',
    # toolHeadBuzzSaw
    '%material Buzzsaw Blade': '%material製丸ノコ刃',
    # turbineBlade
    '%material Turbine Blade': '%material製タービンブレード',
    # itemCasing
    '%material Casing': '%materialのケース',
    # wireFine
    'Fine %material Wire': '%materialのファインワイヤー',
    # gearGtSmall
    'Small %material Gear': '小さな%materialの歯車',
    # rotor
    '%material Rotor': '%materialのローター',
    # stickLong
    'Long %material Rod': '長い%materialの棒',
    'Long %material Stick': '長い%materialの棒', # wood-like
    # springSmall
    'Small %material Spring': '小さな%materialのバネ',
    # spring
    '%material Spring': '%materialのバネ',
    # arrowGtWood
    '%material Arrow': '%materialの矢',
    # arrowGtPlastic
    'Light %material Arrow': '軽い%materialの矢',
    # gemChipped
    'Chipped %material': '欠けた%material',
    'Chipped %material Crystal': '欠けた%materialの結晶', # glass-like
    # gemFlawed
    'Flawed %material': '傷のある%material',
    'Flawed %material Crystal': '傷のある%materialの結晶', # glass-like
    # gemFlawless
    'Flawless %material': '傷のない%material',
    'Flawless %material Crystal': '傷のない%materialの結晶', # glass-like
    # gemExquisite
    'Exquisite %material': '精巧な%material',
    'Exquisite %material Crystal': '精巧な%materialの結晶', # glass-like
    # gearGt
    '%material Gear': '%materialの歯車',
    # crateGtDust
    'Crate of %material Dust': '%materialの粉のクレート',
    'Crate of %material Pulp': '%materialのパルプのクレート', # polymer
    'Crate of %material Powder': '%materialの粉のクレート', # food
    'Crate of %material Crystal Powder': '%materialの結晶の粉のクレート', # Thaumcraft
    # crateGtIngot
    'Crate of %material Ingot': '%materialインゴットのクレート',
    'Crate of %material Bar': '%materialバーのクレート', # polymer
    # crateGtGem
    'Crate of %material': '%materialのクレート',
    'Crate of Shard of %material': '%materialの結晶のクレート', # Thaumcraft
    'Crate of %material Crystal': '%materialの結晶のクレート', # glass-like
    # crateGtPlate
    'Crate of %material Plate': '%materialプレートのクレート',
    'Crate of %material Sheet': '%materialシートのクレート', # polymer
    'Crate of %material Crystal Plate': '%materialの結晶のプレートのクレート', # Thaumcraft
    'Crate of %material Plank': '%materialの板のクレート', # wood-like
    'Crate of %material Pane': '%material板のクレート', # glass-like
    # nanite
    '%material Nanites': '%materialのナナイト',
    # cellMolten
    'Molten %material Cell': '熔融%materialのセル',
    # cellHydroCracked1
    'Lightly Hydro-Cracked %material Cell': '軽く水素で分解された%materialのセル',
    # cellHydroCracked2
    'Moderately Hydro-Cracked %material Cell': '適度に水素で分解された%materialのセル',
    # cellHydroCracked3
    'Severely Hydro-Cracked %material Cell': '十分に水素で分解された%materialのセル',
    # cellSteamCracked1
    'Lightly Steam-Cracked %material Cell': '軽く蒸気で分解された%materialのセル',
    # cellSteamCracked2
    'Moderately Steam-Cracked %material Cell': '適度に蒸気で分解された%materialのセル',
    # cellSteamCracked3
    'Severely Steam-Cracked %material Cell': '十分に蒸気で分解された%materialのセル',
}

formula_to_replace = {
    'No Horses were harmed for the Production': '原材料にウマを含まない', # Glue
    'A chemically approved glue!': '化学的に認められた接着剤！', # AdvancedGlue
    'Accelerates the Mass Fabricator': '物質製造機の稼働速度を向上させる', # UUAmplifier
    'The formula is too long...': '組成を表示するには余白が狭すぎる', # ElectrumFlux
    'Reality itself distilled into physical form': '現実そのものが物質として抽出された', # SpaceTime
    'A tear into the space beyond space': '時空間を超越した裂け目', # Universium
    # '[-Stellar-Stellar-]': '', # ExcitedDTSC
    # 'Stellar': '', # DimensionallyTranscendentStellarCatalyst
}

def main():
    with open('GregTech.lang', 'r', encoding="utf-8") as f:
        lines = f.read().splitlines()
    properties = []
    rest = []
    in_languagefile_category = False
    found_material = False
    for line in lines:
        if not in_languagefile_category:
            if line.startswith("languagefile {"):
                in_languagefile_category = True
            continue

        # in_languagefile_category == True
        if line.startswith("}"):
            break
        split = line.split("=", 1)
        if len(split) != 2:
            found_material = False
            continue
        key = split[0]
        s_key = f"gt-lang|{key}"
        value = split[1]

        if found_material and key.endswith('.tooltip'):
            if value in formula_to_replace:
                formula = formula_to_replace[value]
            else:
                formula = value
            properties.append({
                'key': s_key,
                'original': value,
                'translation': formula,
                'stage': 5,
                'context': s_key + '=' + value,
            })
            found_material = False
            continue

        found_material = False

        if '%material' not in value:
            continue

        if value in to_replace:
            properties.append({
                'key': s_key,
                'original': value,
                'translation': to_replace[value],
                'stage': 5,
                'context': s_key + '=' + value,
            })
            found_material = True
        else:
            rest.append(s_key + '=' + value)

    with open('gtlang.txt', mode="wt", encoding="utf-8") as f:
        for line in properties:
            f.write(line['context'] + '\n')

    with open('GregTech.lang.json', mode="wt", encoding="utf-8") as f:
        json.dump(properties, f, ensure_ascii=False, indent=2)

    with open('rest.txt', mode="wt", encoding="utf-8") as f:
        for line in rest:
            f.write(line + '\n')

if __name__ == '__main__':
    main()
