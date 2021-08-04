# Snakemake workflow management.
## Testing in RNA-seq 
> youtube address: https://www.youtube.com/watch?v=_wUGzqEjg6A

### snakefile.py
```
import os
import glob

# These wildcards are in the files that will be called in and used throughout the programs within the pipeline.
SRR,FRR = glob_wildcards("rawReads/{sra}_{frr}.fastq")

rule all:
    input:
        expand("rawQC/{sra}_{frr}_fastqc.{extension",sra=SRA,frr=FRR, extension=["zip","html"]})
        expand("starAligned/{sra}Aligned.sortedByCoord.out.bam",sra=SRA)

rule rawFastqc:
    input:
        rawread="rawReads/{sra}_{frr}.fastq"
    output:
        zip="rawQC/{sra}_{frr}_fastqc.zip",
        html="rawQC/{sra}_{frr}_fastqc.html"
    threads:
        1
    params:
        path="rawQC/"
    shell:
        """
        fastqc {input.rawread} --threads {threads} -o {params.path}
        """

rule trimmomatic:
    input:
        read1="rawReads/{sra}_1.fastq",
        read2="rawReads/{sra}_2.fastq"
    output:
        forwardPaired="trimmedReads/{sra}_1P.fastq",
        reversePaired="trimmedReads/{sra}_2P.fastq"
    threads:
        4
    params:
        basename="trimmedReads/{sra}.fastq",
        log="trimmedReads/{sra}.log"
    shell:
        """
        trimmomatic PE -threads {threads} {input.read1} {input.read2} -baseout {params.basename} ILLUMINACLIP:* LEADING:3 TRAILING:3 MINLEN:36 2> {params.log}
        """

# We will be calling files from the trimmomatic output. And use it as input.
# Note that it uses 'rules.trimmomatic.output' in the input.
rule star:
    input:
        read1=rules.trimmomatic.output.forwardPaired,  
        read2=rules.trimmomatic.output.reversePaired    
    output:
        bam="starAligned/{sra}Aligned.sortedByCoord.out.bam",
        log="starAligned/{sra}Log.final.out
        
    threads:
        16
    params:
        prefix="starAligned/{sra}"
    shell:
        """
        STAR --runThreadN {threads} --genomeDir starIndex --genomeLoad LoadAndKeep --readFilesIn {input.read1} {input.read2} --outFilterIntronMotifs RemoveNoncanonical --outFileName {params.prefix} --outSAMtypeBAM SortedByCoordinate --limitBAMsortRAM 5000000000 --outReadsUnmapped Fastq
        """

rule star_remove_genome:
    shell:
        """
        STAR --genomeDir starIndex --genomeLoad Remove
        """
```

## Running a dry run.
```
snakemake -s snakfile.py -n

# -s is for the snakefile name when it is not 'snakefile'. We use *.py for the text editor to pick up colors.
# -n is for the DRY RUN.
```

There will be job counts that will print out the texts of rules that will launch.
### output:
```
count   jobs
1   all
2X  fastqc
X   trimmomatic
X   star
```
note: **X** is the number of SRR and since they had paired-end sequences FRR makes it **2X** for fastqc only.

## In real run
```
snakemake -s snakefile.py -j 64

# -j is for the number of cores used for the analysis
```