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
    alert(currentQNum);
    $('input[name="Questions_Num"]').val(currentQNum + 1);
  })
  // Add Choices Event.
  $(document).on('click', 'label[class^="Add-QChoice"]', function() {

  })
  //
  $(document).on('click', 'input[class^="ChoicesRadio"]', function() {
    var fieldNum = this.className.split('-')[1];
    $('div[class^="Q' + fieldNum + '-Choices"]').addClass('flex-column');
    $('div[class^="Q' + fieldNum + '-Choices"]').removeClass('hidden');
    $('input[name^="Q' + fieldNum + '_CH"]').attr('required', 'required');
  })

})

/*
X 1- Show SideBar. X
2- Add Question.
3- Add Choice.
4- ClickOn RadioButton Free-Number-Date.
5- ClickOn RadioButton Choice.
6- Check Username in Ragister page.
7-
*/

/*
var QElem = '<div class="QField-' + fieldNum + ' field flex-column w-90">\
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
            <input class="FreeRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '" checked>\
          </div>\
          <div class="field w-25">\
            <label class="lbl">Number</label>\
            <input class="NumberRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '">\
          </div>\
          <div class="field w-25">\
            <label class="lbl">Date</label>\
            <input class="DateRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '">\
          </div>\
          <div class="field w-25">\
            <label class="lbl">Choices</label>\
            <input class="ChoicesRadio-' + fieldNum + '" type="radio" name="AnswerType_' + fieldNum + '">\
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
*/
