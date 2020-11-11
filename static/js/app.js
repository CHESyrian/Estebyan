$(document).ready(function() {
  // Show SideBar Event.
  $('.Sandwish').click(function() {
    $('.SideBar').toggleClass('w-15');
    $('.Content').toggleClass('w-85');
  })
  // Addd Question Field Event.
  $('.Add-QField').click(function() {
    var fieldNum = $('div[class^="QField"]').length + 1;
    var QElem = '\
      <div class="QField-' + fieldNum + ' field flex-column w-90">\
        <div class="field flex-row w-90">\
          <label class="lbl w-20" for="Q' + fieldNum + '_Input">Question ' + fieldNum + ' :</label>\
          <input class="npt flex-grow" type="text" name="Q' + fieldNum + '_Input" required>\
        </div>\
        <div class="field flex-row w-90">\
          <label class="lbl w-20" for="Keyword1_Input">Keyword </label>\
          <input class="npt flex-grow" type="text" name="Keyword' + fieldNum + '_Input" placeholder="Short word to use as column name in table (ex. Age, Gender, Country, Job)" required>\
        </div>\
        <div class="field flex-row w-90">\
          <div class="field w-25">\
            <label class="lbl">Free</label>\
            <input class="FreeRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '" value="text" checked>\
          </div>\
          <div class="field w-25">\
            <label class="lbl">Number</label>\
            <input class="NumberRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '" value="number">\
          </div>\
          <div class="field w-25">\
            <label class="lbl">Date</label>\
            <input class="DateRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '" value="date">\
          </div>\
          <div class="field w-25">\
            <label class="lbl">Choices</label>\
            <input class="ChoicesRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '" value="select">\
          </div>\
        </div>\
        <div class="Q' + fieldNum + '-Choices field justify-center w-90 hidden">\
          <div class="QChoice-' + fieldNum + '-1 field flex-row w-100">\
            <label class="lbl w-20" for="Q' + fieldNum + '_CH1_Input">Choice 1 :</label>\
            <input class="npt flex-grow" type="text" name="Q' + fieldNum + '_CH1_Input">\
          </div>\
          <label class="Add-QChoice-' + fieldNum + ' lbl lbl-add w-85 justify-center hover-aaa">+Add Choice</label>\
          <input type="hidden" name="Q' + fieldNum + '_Choices_Num" value="1">\
        </div>\
      </div>';
    $('#Q-Form').append(QElem);
    var currentQNum = Number($('input[name="Questions_Num"]').val());
    $('input[name="Questions_Num"]').val(currentQNum + 1);
  })
  // Add Choices Event.
  $(document).on('click', 'label[class^="Add-QChoice"]', function() {
    var fieldNum = this.className.split(' ')[0].split('-')[2];
    var choiceNum = Number($('input[name="Q' + fieldNum + '_Choices_Num"]').val()) + 1;
    alert(choiceNum);
    var choice = '\
      <div class="QChoice-' + fieldNum + '-' + choiceNum + ' field flex-row w-100">\
        <label class="lbl w-20" for="Q' + fieldNum + '_CH' + choiceNum + '_Input">Choice ' + choiceNum + ' :</label>\
        <input class="npt flex-grow" type="text" name="Q' + fieldNum + '_CH' + choiceNum + '_Input" required>\
      </div>';
    $('label[class^="Add-QChoice-' + fieldNum + '"]').before(choice);
    $('input[name="Q' + fieldNum + '_Choices_Num"]').val(choiceNum);
  })
  // Show Choice Field.
  $(document).on('click', 'input[class^="ChoicesRadio"]', function() {
    var fieldNum = this.className.split('-')[1];
    $('div[class^="Q' + fieldNum + '-Choices"]').addClass('flex-column');
    $('div[class^="Q' + fieldNum + '-Choices"]').removeClass('hidden');
    $('input[name^="Q' + fieldNum + '_CH"]').attr('required', 'required');
  })
  // Hide Choice Field.
  $(document).on('click', 'input[class^="FreeRadio"], input[class^="NumberRadio"], input[class^="DateRadio"]', function() {
    var fieldNum = this.className.split('-')[1];
    $('div[class^="Q' + fieldNum + '-Choices"]').removeClass('flex-column');
    $('div[class^="Q' + fieldNum + '-Choices"]').addClass('hidden');
    $('input[name^="Q' + fieldNum + '_CH"]').removeAttr('required');
  })

})

/*
X 1- Show SideBar. X
X 2- Add Question. X
X 3- Add Choice. X
X 4- ClickOn RadioButton Free-Number-Date. X
X 5- ClickOn RadioButton Choice. X
6- Check Username in Ragister page.
7-
*/
