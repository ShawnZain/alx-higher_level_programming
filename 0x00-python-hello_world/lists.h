#ifndef LISTS_H
#define LISTS_H

/******LIBRARIES******/
#include <stdlib.h>
#include <stdio.h>

/******STRUCT******/
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/******PROTOTYPES******/
int check_cycle(listint_t *list);

#endif /* LIST_H */
