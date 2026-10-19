# Illusztrációk

Ide kerülnek a fejezetekhez tartozó illusztrációk promptjai és az elkészült képek. A képeket a szöveg kész állapotában szerkesztjük a fejezetekbe (a munkamód 4. lépésénél), addig csak ebben a mappában vannak.

## Elnevezés

`FF-SS-cim.md` a prompt, mellette ugyanezzel a névvel `.png` a kész kép. `FF` a fejezet sorszáma, `SS` a kép sorszáma a fejezeten belül.

## Hogyan épülnek a promptok

Minden prompt rögzíti: a kameraállást, az előteret, a középteret és a hátteret, a bal és jobb oldalt (mindig a néző szemszögéből), azt, hogy ki hol ül vagy áll, merre néz, és milyen irányba állnak a székek. A végén egy `DO NOT` sor felsorolja, amit a generátor ne tegyen. A promptok szándékosan hosszúak.

A helyszínek és a ruhák rögzített leírása a `helyszinek-es-szereplok.md` fájlban van, minden prompt ezekből építkezik. Ha egy generátor mégis elrontja a térbeli elrendezést (például a székeket az asztalnak háttal rakja), írd át a promptot a következő módon: ismételd meg a hibás részt, és fogalmazd meg ellentétes irányban („the chairs face the table, the sitters face each other").

## Generátor: Microsoft Create

A képek a Microsoft Create (Designer) segítségével készülnek. Két dolgot nem tudtam ellenőrizni, ezért próbáld ki: mekkora promptot fogad el a beviteli mező, és elfogadja-e a valós személyek neveit. Ezért minden promptfájlban van két változat:

- **Hosszú prompt:** minden térbeli részlet benne van. Ezt használd, ha a mező elfogadja.
- **Rövid változat (kb. 300–450 karakter):** ha a mező levágja a hosszú promptot, ezt másold be, és a hiányzó részleteket (ki hol ül) szükség esetén egy-egy mondattal pótold.

A promptok szövegében nincs valós név: a szereplők külsejét ruha és mozdulat adja, a nevek csak a promptfájlok végén vannak megjegyzésként. Ha van képarány-választó, válaszd a fekvő (3:2 vagy 16:9) formátumot.

## Közös stílus

Minden prompt ugyanazzal a mondattal indul, így a képek egységesek lesznek:

> Monochrome graphite pencil drawing on cream paper, hand-hatched, soft smudged shading, fine paper grain, soft vignette edges, ominous gothic mood.

Tippek az egységességhez:

- Ugyanazt a generátort használd az összes képhez, és kérj 3:2 fekvő formátumot.
- Ha a generátor színt vagy fotót ad, tedd a prompt elejére: „black and white only, pencil on paper, not a photo".
- Negatív prompt, ha támogatja: `color, watercolor, photograph, 3D render, cartoon, anime, text, caption, signature, watermark`.
- Olvasható feliratot a generátorok rosszul írnak, ezért a promptok szándékosan olvashatatlan feliratot kérnek.
- Ha egy generátor elutasítja a valós személyek nevét, cseréld a nevet korhű ruhaleírásra („a man in a 1950s dark suit and tie"), és a jellegzetes mozdulatot hagyd benne. A mozdulat a szereplő modorát hordozza, az arc felismerhetősége nem fontos.
- A szereplőket méltósággal ábrázold, karikatúra nélkül. A könyv humora a szövegben van, a képek komolyak.

## Képek

| Fájl | Kapcsolódó mondat | Kész |
|------|-------------------|------|
| `01-01-holdvari-kastely` | „A Holdvári-kastély a dombtetőn állt…" | rajz kész (vagy generátorral) |
| `01-02-a-jatekmester-az-erkelyen` | „…az erkélyen egyetlen fénysugár villant fel…" | |
| `01-03-a-hideg-ujj` | „Aztán hideg ujj érintette a vállát…" | |
| `01-04-a-konklave` | „A gyertya lángja meghajolt…" | |
| `02-01-az-elporladt-nevtabla` | „…a betűk szélei elporladtak…" | |
| `02-02-a-labirintus-bejarata` | „A bejáratnál kőív állt…" | |
| `02-03-bud-spencer-atmegy-a-soveny-falon` | „A tiszafa először nem engedett, aztán mégis." | |
| `02-04-latabar-a-kuszobon` | „A küszöbön megbotlott…" | |
| `03-01-a-csend-szalonja` | „A terem közepén hatalmas álló óra állt…" | |
| `03-02-mercury-tenyere` | „A ceruzával írt név már nem látszott…" | |
| `03-03-psota-iren-a-pajzzsal` | „…mintha kígyót fogna." | |
