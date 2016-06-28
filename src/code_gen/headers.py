__author__="apoorvKumar"

HEADER_DATA = """
#include <stdio.h>
#define TRUE 1
#define FALSE 0
#define CLK_TCK 100

struct DummyStruct
{
int st_var_int;
float st_var_flt;
char st_var_char;
double st_var_db;
};

#define ALLOC_TEST_MAGIC 0x72ec82d2

/* This value is written to memory after it is freshly allocated, to ensure
 * that code under test does not rely on memory being initialised by
 * malloc(). */

#define MALLOC_PATTERN 0xBAADF00D

/* This value is written to memory after it is freed, to ensure that code
 * does not rely on memory that has been freed. */

#define FREE_PATTERN 0xDEADBEEF

/**
 * All blocks allocated by the testing framework are preceded by a structure
 * of this type.
 */

typedef struct _BlockHeader BlockHeader;

struct _BlockHeader {
    unsigned int magic_number;
    size_t bytes;
};


"""
