#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert new node to am ordered singly
 * linked list
 * @head: pointer to address of head node
 * @number: integer value of the new inserted node
 *
 * Return: pointer to node or NULL if error occurs
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head, *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (head == NULL || new == NULL)
		return (NULL);
	new->n = number;
	if (temp == NULL)
	{
		new->next = NULL;
		return (new);
	}
	for (; temp->next != NULL && temp->n < number;)
	{
		prev = temp;
		temp = temp->next;
	}
	if (temp->n > number)
	{
		if (prev == NULL)
			new->next = temp;
		else
		{
			prev->next = new;
			new->next = temp;
		}
	}
	else
	{
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}

