export const HomePage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto bg-white shadow-xl rounded-2xl overflow-hidden border border-slate-200">

        <div className="p-8 space-y-7 text-slate-700 leading-relaxed">

          <p className="text-lg font-medium text-slate-800">
            Разработанная программа предназначена для автоматизированного расчёта коэффициентов модели динамического объекта на основе экспериментально полученной кривой разгона. Этот процесс включает в себя несколько ключевых этапов.
          </p>

          <div className="bg-blue-50 border-l-4 border-blue-400 p-5 rounded-r-lg shadow-sm">
            <h2 className="text-xl font-semibold text-blue-800 mb-3">Ввод и предварительная обработка данных</h2>
            <p>
              Программа позволяет вводить экспериментальные данные, представляющие собой зависимость выходного параметра объекта от времени. После ввода данных программа приступает к их обработке. Сначала выполняется предварительная фильтрация и сглаживание данных для устранения случайных шумов и выбросов, что критически важно для обеспечения точности последующих расчётов.
            </p>
          </div>

          <div className="bg-indigo-50 border-l-4 border-indigo-400 p-5 rounded-r-lg shadow-sm">
            <h2 className="text-xl font-semibold text-indigo-800 mb-3">Идентификация параметров модели</h2>
            <p>
              Затем начинается основной этап анализа – идентификация параметров модели объекта. Программа использует методы численного анализа, такие как метод площадей и наименьших квадратов. Результатом этого этапа является получение передаточной функции, описывающей поведение системы.
            </p>
          </div>

          <div className="bg-emerald-50 border-l-4 border-emerald-400 p-5 rounded-r-lg shadow-sm">
            <h2 className="text-xl font-semibold text-emerald-800 mb-3">Графическая визуализация результатов</h2>
            <p>
              Полученные уравнения преобразуются в графическую форму, что позволяет наглядно сравнить экспериментальную кривую разгона и теоретическую модель. Программа строит графики, отображающие как исходные данные, так и аппроксимирующую их модельную кривую. Такой визуальный подход помогает пользователю оценить качество подгонки модели и выявить возможные отклонения.
            </p>
          </div>

          <div className="bg-amber-50 border-l-4 border-amber-400 p-5 rounded-r-lg shadow-sm">
            <h2 className="text-xl font-semibold text-amber-800 mb-3">Числовые характеристики модели</h2>
            <p>
              Помимо графического представления, программа выводит числовые значения параметров модели. Эти параметры включают усиление, постоянные времени и другие характеристики, необходимые для полной оценки динамического поведения объекта.
            </p>
          </div>

          <div className="bg-purple-50 border-l-4 border-purple-400 p-5 rounded-r-lg shadow-sm">
            <h2 className="text-xl font-semibold text-purple-800 mb-3">Настройка регуляторов</h2>
            
            <p className="mb-4">
              Программа автоматически определяет оптимальный тип регулятора на основе характера технологического процесса и обеспечивает расчёт его настроечных коэффициентов.
            </p>

            <div className="bg-white p-4 rounded-lg border border-slate-200 mb-4">
              <h3 className="font-semibold text-slate-800 mb-3 text-center">Алгоритм автоматического выбора типа регулятора</h3>
              <div className="space-y-3">
                <div className="flex items-start p-3 rounded-lg bg-blue-50 border border-blue-100">
                  <div className="bg-blue-100 text-blue-800 px-3 py-1 rounded mr-3 text-sm font-medium min-w-[70px] text-center">P-регулятор</div>
                  <div>
                    <span className="font-medium text-blue-800">Используется для контуров:</span> <span className="font-medium">"Промежуточная емкость"</span>, <span className="font-medium">"Емкость хранения"</span>
                    <p className="text-sm text-slate-600 mt-1">Простые системы с минимальными требованиями к точности, где достаточно пропорционального регулирования.</p>
                  </div>
                </div>
                
                <div className="flex items-start p-3 rounded-lg bg-green-50 border border-green-100">
                  <div className="bg-green-100 text-green-800 px-3 py-1 rounded mr-3 text-sm font-medium min-w-[70px] text-center">PI-регулятор</div>
                  <div>
                    <span className="font-medium text-green-800">Используется по умолчанию для большинства процессов</span>
                    <p className="text-sm text-slate-600 mt-1">Обеспечивает точность регулирования без избыточной сложности, устраняя установившуюся ошибку.</p>
                  </div>
                </div>
                
                <div className="flex items-start p-3 rounded-lg bg-red-50 border border-red-100">
                  <div className="bg-red-100 text-red-800 px-3 py-1 rounded mr-3 text-sm font-medium min-w-[70px] text-center">PID-регулятор</div>
                  <div>
                    <span className="font-medium text-red-800">Используется для контуров:</span> <span className="font-medium">"Температура"</span>
                    <p className="text-sm text-slate-600 mt-1">Сложные объекты с высокой инерционностью и требованиями к быстродействию, где необходима дифференциальная составляющая.</p>
                  </div>
                </div>
              </div>
            </div>

            <p>
              В зависимости от требований к системе программа анализирует динамические характеристики (устойчивость, время переходного процесса, перерегулирование) и с помощью методов численного моделирования и оптимизации определяет оптимальные параметры регулятора:
            </p>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 my-4">
              <div className="bg-blue-50 p-4 rounded-lg border border-blue-200 text-center">
                <div className="text-blue-800 font-semibold mb-2">П-регулятор</div>
                <div className="font-mono bg-white py-2 rounded border">Kp</div>
                <div className="text-sm text-slate-600 mt-1">пропорциональный коэффициент</div>
              </div>
              <div className="bg-green-50 p-4 rounded-lg border border-green-200 text-center">
                <div className="text-green-800 font-semibold mb-2">ПИ-регулятор</div>
                <div className="font-mono bg-white py-2 rounded border">Kp, Ki</div>
                <div className="text-sm text-slate-600 mt-1">пропорциональный и интегральный коэффициенты</div>
              </div>
              <div className="bg-red-50 p-4 rounded-lg border border-red-200 text-center">
                <div className="text-red-800 font-semibold mb-2">ПИД-регулятор</div>
                <div className="font-mono bg-white py-2 rounded border">Kp, Ki, Kd</div>
                <div className="text-sm text-slate-600 mt-1">пропорциональный, интегральный и дифференциальный коэффициенты</div>
              </div>
            </div>

            <p>
              Для каждого типа регулятора вычисляются коэффициенты, обеспечивающие баланс между быстродействием, стабильностью и точностью, минимизируя установившуюся ошибку и оптимизируя отклик системы на управляющие воздействия и возмущения.
            </p>
          </div>

          <div className="bg-slate-50 border-l-4 border-slate-400 p-5 rounded-r-lg shadow-sm">
            <h2 className="text-xl font-semibold text-slate-800 mb-3">Преимущества программы</h2>
            <ul className="list-disc list-inside space-y-2">
              <li>Экономия времени и ресурсов — автоматизация расчётов устраняет необходимость в трудоёмких и подверженных ошибкам ручных вычислениях.</li>
              <li>Высокая точность — снижается вероятность человеческих ошибок, что особенно важно в сложных инженерных задачах.</li>
              <li>Автоматический выбор регулятора — интеллектуальный подбор оптимальной структуры регулятора на основе типа технологического процесса.</li>
              <li>Универсальность — поддержка расчёта параметров для трёх типов регуляторов (П, ПИ, ПИД).</li>
              <li>Удобство — позволяет инженерам быстро и надёжно получать настройки регуляторов, сосредоточившись на интеграции и тонкой доводке системы.</li>
            </ul>
          </div>

          <div className="text-center mt-8 pt-6 border-t border-slate-200">
            <p className="text-slate-600 italic">
              Таким образом, программа значительно облегчает процесс определения динамических характеристик объекта и последующего синтеза систем управления. Она не только ускоряет процесс анализа, но и делает его более точным, воспроизводимым и удобным.
            </p>
          </div>

        </div>

      </div>
    </div>
  );
};