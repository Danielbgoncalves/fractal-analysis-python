import os
import shutil
from math import ceil

# ===== CONFIGURAÇÕES =====
ORIGINAIS_DIR = "originais"
RECPLOT_DIR = "F-RecPlot"
OUTPUT_DIR = "dataset_pulmao"

CLASSES = ["aca_md", "nor", "scc_md"]
TEST_RATIO = 0.2  # 20% teste

# =========================


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def copy_pair(orig_path, rec_path, dest_orig_dir, dest_rec_dir):
    ensure_dir(dest_orig_dir)
    ensure_dir(dest_rec_dir)

    shutil.copy2(orig_path, dest_orig_dir)
    shutil.copy2(rec_path, dest_rec_dir)


for cls in CLASSES:
    print(f"\nProcessando classe: {cls}")

    orig_cls_dir = os.path.join(ORIGINAIS_DIR, cls)
    rec_cls_dir = os.path.join(RECPLOT_DIR, cls)

    orig_files = sorted(
        [f for f in os.listdir(orig_cls_dir) if f.lower().endswith(".jpg")]
    )

    rec_files = sorted(
        [f for f in os.listdir(rec_cls_dir) if f.lower().endswith(".png")],
        key=lambda x: int(os.path.splitext(x)[0])  # 1.png, 2.png, ...
    )

    assert len(orig_files) == len(rec_files), (
        f"Quantidade diferente em {cls}: "
        f"{len(orig_files)} originais vs {len(rec_files)} recplot"
    )

    total = len(orig_files)
    n_test = ceil(total * TEST_RATIO)

    print(f"Total: {total} | Teste: {n_test} | Treino+Val: {total - n_test}")

    for i, (orig_name, rec_name) in enumerate(zip(orig_files, rec_files)):
        split = "teste" if i < n_test else "treino_e_validacao"

        dest_orig_dir = os.path.join(
            OUTPUT_DIR, split, cls, "originais"
        )
        dest_rec_dir = os.path.join(
            OUTPUT_DIR, split, cls, "F-RecPlot"
        )

        orig_path = os.path.join(orig_cls_dir, orig_name)
        rec_path = os.path.join(rec_cls_dir, rec_name)

        copy_pair(orig_path, rec_path, dest_orig_dir, dest_rec_dir)

print("\n✅ Dataset criado com sucesso!")
