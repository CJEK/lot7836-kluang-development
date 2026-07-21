"""Generate the English Lot 7836 concept drawing PDF and editable DXF sources.

These artefacts are deliberately marked NOT FOR CONSTRUCTION / NOT FOR SUBMISSION.
They provide controlled concept communication, not signed construction documents.
"""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables"
DXF = OUT / "dxf"
PREVIEWS = ROOT / "assets" / "drawings"
PDF = OUT / "lot7836-concept-drawing-set.pdf"
PAGE_W, PAGE_H = landscape(A3)

CONTROL = "50ft x 75ft | 2 x 40ft HC (8ft wide) | 34ft hall | 35ft rear steel zone | 30 deg roof | +24ft eave | +38ft-5in ridge | +47ft Jack Roof"
SHEETS = [
    ("A-101", "ARCHITECTURAL FLOOR PLAN", "Plan control diagram: two longitudinal 40ft HC containers, a 34ft hall and rear 35ft steel zone."),
    ("A-102", "FRONT ELEVATION AND LEVEL CONTROL", "Level control diagram: +24ft eave, +38ft-5in main ridge, +47ft Raised Jack Roof."),
    ("S-101", "CONTAINER MODIFICATION REVIEW", "Concept-only cut-out reinforcement review. Member sizes, welding and connections require structural design."),
    ("M-101", "WET-CORE DRAINAGE REVIEW", "Concept sanitary coordination. Pipe sizes, vents, invert levels and public connection require MEP design."),
    ("F-101", "FIRE AND EGRESS REVIEW", "Concept review checklist only. Egress, appliances, travel distance and appliance access require BOMBA review."),
    ("T-101", "TESTING AND COMMISSIONING REVIEW", "Proposed test subjects only. Test methods, acceptance criteria and records require professional confirmation."),
    ("G-101", "SITE REVIEW PLAN", "Survey, setbacks, fire access, drainage outfall and sanitary solution remain pending official confirmation."),
]


def header(c, number, title):
    c.setFillColor(colors.HexColor("#142235")); c.rect(24, PAGE_H - 68, PAGE_W - 48, 44, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 18); c.drawString(42, PAGE_H - 52, f"LOT 7836 KLUANG | {number} | {title}")
    c.setStrokeColor(colors.HexColor("#B86618")); c.setLineWidth(1.2); c.line(42, PAGE_H - 84, PAGE_W - 42, PAGE_H - 84)


def footer(c, number):
    c.setFillColor(colors.HexColor("#142235")); c.rect(24, 24, PAGE_W - 48, 72, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#FFFFFF")); c.setFont("Helvetica-Bold", 9)
    c.drawString(40, 74, "STAGE: CONCEPT DESIGN - NOT FOR CONSTRUCTION / NOT FOR SUBMISSION")
    c.setFont("Helvetica", 7.5); c.drawString(40, 58, "Professional review required: Ar. / P.Eng / MPK / BOMBA / IWK. Drawing is diagrammatic and not to scale.")
    c.drawRightString(PAGE_W - 40, 74, f"SHEET: {number}")
    c.drawRightString(PAGE_W - 40, 58, "REV: 01 | 21 JUL 2026")


def wrapped(c, text, x, y, width, leading=15):
    words, line = text.split(), ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if stringWidth(candidate, "Helvetica", 10) > width:
            c.drawString(x, y, line); y -= leading; line = word
        else: line = candidate
    if line: c.drawString(x, y, line)
    return y


def diagram(c, number):
    x, y, w, h = 85, 170, PAGE_W - 170, 340
    c.setStrokeColor(colors.HexColor("#6E849B")); c.setLineWidth(1); c.rect(x, y, w, h, fill=0, stroke=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(colors.HexColor("#142235"))
    if number == "A-101":
        scale_x, scale_y = w / 50, h / 75
        c.setStrokeColor(colors.HexColor("#B86618")); c.rect(x, y + h - 40 * scale_y, 8 * scale_x, 40 * scale_y, fill=0)
        c.rect(x + 42 * scale_x, y + h - 40 * scale_y, 8 * scale_x, 40 * scale_y, fill=0)
        c.setFillColor(colors.HexColor("#166A5B")); c.rect(x + 8 * scale_x, y + h - 40 * scale_y, 34 * scale_x, 40 * scale_y, fill=1, stroke=0)
        c.setFillColor(colors.white); c.drawCentredString(x + 25 * scale_x, y + h - 20 * scale_y, "34ft DOUBLE-HEIGHT HALL")
        c.setFillColor(colors.HexColor("#142235")); c.drawString(x + 7, y + h - 25, "40ft HC"); c.drawRightString(x + w - 7, y + h - 25, "40ft HC")
        c.setStrokeColor(colors.HexColor("#B86618")); c.line(x, y - 12, x + w, y - 12); c.drawCentredString(x + w / 2, y - 27, "50ft FRONTAGE")
        c.line(x - 12, y, x - 12, y + h); c.saveState(); c.translate(x - 27, y + h / 2); c.rotate(90); c.drawCentredString(0, 0, "75ft DEPTH"); c.restoreState()
        c.setFillColor(colors.HexColor("#142235")); c.drawCentredString(x + w / 2, y + 35, "35ft REAR STEEL EXTENSION / 900 sqft LOFT CONCEPT ZONE")
    elif number == "A-102":
        base = y + 30; eave = base + 150; ridge = eave + 90; jack = ridge + 62
        c.setStrokeColor(colors.HexColor("#142235")); c.line(x + 50, base, x + w - 50, base)
        c.line(x + 100, eave, x + w / 2, ridge); c.line(x + w / 2, ridge, x + w - 100, eave)
        c.rect(x + w / 2 - 85, ridge, 170, jack - ridge, fill=0)
        for level, label in [(base, "FL +/-0.00"), (eave, "+24ft EAVE"), (ridge, "+38ft-5in RIDGE"), (jack, "+47ft JACK ROOF")]:
            c.setStrokeColor(colors.HexColor("#B86618")); c.line(x + 20, level, x + w - 20, level); c.setFillColor(colors.HexColor("#142235")); c.drawString(x + 25, level + 4, label)
        c.drawCentredString(x + w / 2, eave + 38, "30 DEG ROOF PITCH ACROSS 50ft SPAN")
    elif number == "S-101":
        c.setFillColor(colors.HexColor("#EEF3F6")); c.rect(x + 80, y + 45, 180, h - 90, fill=1, stroke=0)
        c.setStrokeColor(colors.HexColor("#B86618")); c.setLineWidth(5); c.rect(x + 255, y + 65, 80, h - 130, fill=0)
        c.setStrokeColor(colors.HexColor("#142235")); c.setLineWidth(1); c.rect(x + 80, y + 45, 180, h - 90, fill=0)
        c.setFont("Helvetica-Bold", 10); c.setFillColor(colors.HexColor("#142235")); c.drawString(x + 100, y + h - 35, "CONTAINER WALL")
        c.drawString(x + 270, y + h - 35, "RHS CONCEPT FRAME")
        c.setFont("Helvetica", 9); c.drawString(x + 370, y + h - 80, "100 x 100mm RHS is a concept assumption only.")
        c.drawString(x + 370, y + h - 100, "Opening, welds, anchors and load path require P.Eng design.")
    elif number == "M-101":
        c.setFillColor(colors.HexColor("#E7F3FA")); c.rect(x + 55, y + 85, 170, 180, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#F9E8E8")); c.rect(x + w - 225, y + 85, 170, 180, fill=1, stroke=0)
        c.setStrokeColor(colors.HexColor("#166A5B")); c.setLineWidth(4); c.line(x + 225, y + 160, x + w - 225, y + 160)
        c.setStrokeColor(colors.HexColor("#B86618")); c.setLineWidth(4); c.line(x + 225, y + 125, x + w - 225, y + 125)
        c.setFillColor(colors.HexColor("#142235")); c.setFont("Helvetica-Bold", 11); c.drawString(x + 80, y + 240, "KITCHEN / GREASE TRAP REVIEW")
        c.drawString(x + w - 205, y + 240, "TWIN WC REVIEW")
        c.setFont("Helvetica", 9); c.drawCentredString(x + w / 2, y + 174, "GREYWATER ROUTE - TO BE DESIGNED")
        c.drawCentredString(x + w / 2, y + 139, "SOIL / WASTE ROUTE - TO BE DESIGNED")
        c.drawString(x + 70, y + 45, "Vent, cleanouts, inspection chambers, gradients, invert levels and final connection are outside this concept sheet.")
    elif number == "F-101":
        c.setStrokeColor(colors.HexColor("#142235")); c.rect(x + 120, y + 55, w - 240, h - 110, fill=0)
        c.setFillColor(colors.HexColor("#DDF4E9")); c.rect(x + w / 2 - 70, y + h - 55, 140, 28, fill=1, stroke=0); c.rect(x + w / 2 - 70, y + 27, 140, 28, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#166A5B")); c.setFont("Helvetica-Bold", 10); c.drawCentredString(x + w / 2, y + h - 46, "EXIT 1 - REVIEW")
        c.drawCentredString(x + w / 2, y + 37, "EXIT 2 / LOFT ESCAPE - REVIEW")
        c.setStrokeColor(colors.HexColor("#166A5B")); c.setLineWidth(3); c.line(x + w / 2, y + 90, x + w / 2, y + h - 90)
        c.setFillColor(colors.HexColor("#142235")); c.setFont("Helvetica", 9); c.drawCentredString(x + w / 2, y + h / 2 + 25, "Egress arrangement and travel distance require BOMBA / fire consultant review.")
        c.drawCentredString(x + w / 2, y + h / 2 + 8, "No smoke detector, extinguisher, appliance access or door width is approved by this diagram.")
    elif number == "T-101":
        tests = ["1  Water pressure", "2  Wet-area flood", "3  Roof spray", "4  Electrical protection", "5  Ventilation performance"]
        for i, test in enumerate(tests):
            xx = x + 50 + (i % 3) * 245; yy = y + 195 - (i // 3) * 125
            c.setFillColor(colors.HexColor("#F2F6F8")); c.rect(xx, yy, 210, 88, fill=1, stroke=0)
            c.setFillColor(colors.HexColor("#142235")); c.setFont("Helvetica-Bold", 9); c.drawString(xx + 12, yy + 52, test)
            c.setFont("Helvetica", 7.5); c.drawString(xx + 12, yy + 34, "Method, criteria and record: professional confirmation required.")
    elif number == "G-101":
        c.setFillColor(colors.HexColor("#F2F6F8")); c.rect(x + 80, y + 55, w - 160, h - 110, fill=1, stroke=0)
        c.setStrokeColor(colors.HexColor("#142235")); c.setLineWidth(1.5); c.rect(x + 180, y + 105, w - 360, h - 210, fill=0)
        c.setFillColor(colors.HexColor("#142235")); c.setFont("Helvetica-Bold", 11); c.drawCentredString(x + w / 2, y + h / 2 + 30, "SITE REVIEW BOUNDARY - 50ft x 75ft")
        c.setFont("Helvetica", 9); c.drawCentredString(x + w / 2, y + h / 2 + 8, "Jalan Pakis orientation, survey boundary, setbacks, fire access and public-drain connection pending confirmation.")
        c.setFillColor(colors.HexColor("#B86618")); c.drawString(x + 95, y + h - 35, "NORTH / ROAD / SETBACKS: TO BE VERIFIED FROM SURVEY AND AUTHORITY CONDITIONS")
    else:
        c.setFillColor(colors.HexColor("#F2F6F8")); c.rect(x + 35, y + 35, w - 70, h - 70, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#142235")); c.setFont("Helvetica-Bold", 16); c.drawCentredString(x + w / 2, y + h / 2 + 16, "CONCEPT REVIEW DIAGRAM")
        c.setFont("Helvetica", 10); c.drawCentredString(x + w / 2, y + h / 2 - 8, "Refer to the PDF notes and registered professionals for final design.")


def dxf_text(code, value): return f"{code}\n{value}\n"


def make_dxf(number, title, description):
    rows = ["0\nSECTION\n2\nHEADER\n0\nENDSEC\n0\nSECTION\n2\nENTITIES\n"]
    for x1, y1, x2, y2 in [(0,0,500,0),(500,0,500,300),(500,300,0,300),(0,300,0,0)]:
        rows.append("0\nLINE\n8\nOUTLINE\n" + dxf_text(10,x1)+dxf_text(20,y1)+dxf_text(11,x2)+dxf_text(21,y2))
    for x, y, text, height in [(20,270,f"LOT 7836 | {number} | {title}",10),(20,240,"CONCEPT DESIGN - NOT FOR CONSTRUCTION / NOT FOR SUBMISSION",7),(20,210,CONTROL,5),(20,180,description,5),(20,150,"Professional review: Ar. / P.Eng / MPK / BOMBA / IWK",5)]:
        rows.append("0\nTEXT\n8\nTEXT\n" + dxf_text(10,x)+dxf_text(20,y)+dxf_text(40,height)+dxf_text(1,text))
    rows.append("0\nENDSEC\n0\nEOF\n")
    (DXF / f"{number.lower()}.dxf").write_text("".join(rows), encoding="ascii")


def main():
    OUT.mkdir(exist_ok=True); DXF.mkdir(exist_ok=True); PREVIEWS.mkdir(exist_ok=True)
    c = canvas.Canvas(str(PDF), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    for number, title, description in SHEETS:
        header(c, number, title); diagram(c, number)
        c.setFillColor(colors.HexColor("#142235")); c.setFont("Helvetica-Bold", 10); c.drawString(85, 130, "DESIGN CONTROL")
        c.setFont("Helvetica", 9); wrapped(c, CONTROL, 85, 114, PAGE_W - 170, 13)
        c.setFont("Helvetica-Bold", 10); c.drawString(85, 102, "SHEET PURPOSE")
        c.setFont("Helvetica", 9); wrapped(c, description, 85, 87, PAGE_W - 170, 13)
        footer(c, number); c.showPage(); make_dxf(number, title, description)
    c.save()
    with ZipFile(OUT / "lot7836-concept-dxf-source.zip", "w", ZIP_DEFLATED) as archive:
        for path in sorted(DXF.glob("*.dxf")): archive.write(path, path.relative_to(OUT))


if __name__ == "__main__": main()
