sequence = "ATCG---CTGNACNGN"

for nucleotide in sequence:
  if nucleotide == "-" or nucleotide == 'N':
    continue
  print(nucleotide, end="")
# > TCGCTGCG

index = 0
while index < len(sequence):
  nucleotide = sequence[index]

  # Noten la posicion del index
  index = index + 1

  if nucleotide == "-" or nucleotide == 'N':
    continue
  print(nucleotide, end="")
# > TCGCTGCG
