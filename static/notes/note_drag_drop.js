new Sortable(noteList, {
    animation: 150,
    ghostClass: 'sortable-ghost',
    update: function(event, ui) {
        // Update the order of notes in the database using AJAX
        var noteIds = $(this).sortable("serialize");
        $.ajax({
            url: '{% url "notes.reorder" %}',
            type: 'POST',
            data: { order: noteIds },
            headers: { 'X-CSRFToken': '{{ csrf_token }}' },
        });
    }
});