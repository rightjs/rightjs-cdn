/**
 * RightJS UI Internationalization: Russian module
 *
 * Copyright (C) Nikolay Nemshilov
 */
if (self.Calendar) {
  $ext(Calendar.i18n, {
    Done:            'Готово',
    Now:             'Сейчас',
    NextMonth:       'Следующий месяц',
    PrevMonth:       'Предыдущий месяц',
    NextYear:        'Следующий год',
    PrevYear:        'Предыдущий год',

    dayNames:        $w('Воскресенье Понедельник Вторник Среда Четверг Пятница Суббота'),
    dayNamesShort:   $w('Вск Пнд Втр Срд Чтв Птн Сбт'),
    dayNamesMin:     $w('Вс Пн Вт Ср Чт Пт Сб'),
    monthNames:      $w('Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь'),
    monthNamesShort: $w('Янв Фев Мар Апр Май Инь Иль Авг Сен Окт Ноя Дек')
  });
}

if (self.Lightbox) {
  $ext(Lightbox.i18n, {
    Close: 'Закрыть',
    Prev:  'Предыдущее изображение',
    Next:  'Следующее изображение'
  });
}

if (self.InEdit) {
  $ext(InEdit.i18n, {
    Save:   "Сохранить",
    Cancel: "Отмена"
  });
}

if (self.Colorpicker) {
  $ext(Colorpicker.i18n, {
    Done: 'Готово'
  });
}

if (self.Dialog) {
  $ext(Dialog.i18n, {
    Ok:       'Готово',
    Close:    'Закрыть',
    Cancel:   'Отмена',
    Help:     'Помощь',
    Expand:   'Во все окно',
    Collapse: 'Обычный размер',

    Alert:    'Внимание!',
    Confirm:  'Подтверждение',
    Prompt:   'Ввод данных'
  });
}