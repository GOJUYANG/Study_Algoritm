# 1. 알고리즘(Algorithm)은 무엇인가?
#  : 어떤 작업을 수행하기 위해 입력을 받아 원하는 출력을 만들어내는 과정을 기술한 것
#  즉, 어떠한 문제를 해결하는 과정 자체가 알고리즘.
#
#
# 2. 알고리즘은 어떻게 설계해야하는가?
#  : 명확하고 효율적으로 설계
#  명확 => 알고리즘을 보는 대상을 위한 속성, 이를 보고 알고리즘의 흐름을 읽을 수 있어야 함.
#  효율 => 입력이 충분히 클 때, 가능한 빠르게 해결할 수 있도록 하는 것.
#
# 3. '생각하는 방법'
#  : 알고리즘은 '어떻게?'라는 질문에 스스로 답변하며 해결해가는 '생각하는 방법'을 만드는 과정.
#  또한 이러한 해결책은 또다른 알고리즘으로 분화되어 사용된다.
#  마치 우리가 사칙연산을 이용하여 삼각형의 넓이를 계산하는 것과 같다.
#  이미 최적화 된 답이 있는 문제도 있지만 세상에 문제가 아직 해결되지 않은 문제가 많다.
#  ex) 최적화 된 답이 이미 있는 문제 : 정렬 문제, 검색 문제 등
#  ex) 정답이 없는 문제 : 유튜브 알고리즘, 광고 추천 알고리즘 등
#  그러나, 이미 정답이 있는 문제 또한 어느 순간 새로운 정답이나 이를 뛰어넘는 경우가 생길 수도 있다.
#
# 4. 알고리즘은 자료구조의 확장
#  : 생각의 전개를 위해 필요한 기본적인 구조.
#  즉, 알고리즘을 진행하기 위한 입력이나 중간단계의 구조를 일컺는 말이다.
#  자료구조를 이해함과 이해하지 못함은 마치 자동차의 헤드라이트가 있음에도 있는지 몰라 등을 따로 다는 것과 같다.
#  자료구조에서 제공가능한 기능은 무엇이며, 이것이 가능 속성이 무엇인지 파악해야만 더 효율적인 알고리즘이 만들어 진다.
# (+) heap, stack, queue
# (+) heap : 완전 이진 트리를 기초로 하며 우선 순위 큐를 위한 자료 구조 (노드)
# (+) stack : last in, first out (후입선출)
# (+) queue : first in, first out (선입선출)

#
# 5. 자료형과 자료구조
#  : 이런 구조를 이해하기 위해서는 자료형에 대해서 이해해야한다.
#  자료구조로 바로 넘어갈 수 있으나, 자료형에 따라 자료구조가 바뀔수도 있다는 점을 생각한다면 쉽게 볼 문제가 아니다.
#  물론 우리가 생각하기에 글자는 글자, 숫자는 숫자로 이해할 수 있으나, 컴퓨터는 이를 오직 이진수의 수로만 인식할 수 있다.
#  이 제한된 이진수를 이용하기 때문에 실질적인 자료구조와 컴퓨터의 자료구조상의 괴리가 발생할 수 있다.
#  이를 해결하기 위해서는 정확한 자료형에 대한 이해가 필요하다.
#  python에서 0.1과 0.2의 합이 0.3이 아닌 수인 것에 대해 정확한 원인을 알고 모르고는 앞으로 모든 수학적 지식이 유의미할 수도 무의미할 수도 있다.
#  (+) 인간은 숫자를 표현하기 위해 10진법을 사용하고 컴퓨터는 2진법을 사용한다. 그 차이에서 비롯된 오차결과
#  (+) 0.1(십진법)을 이진법으로 변환하게 되면 무한 소수로 정확하게 떨어지지 않는다. 고려할 것은 컴퓨터의 메모리는 무한하지 않다.
#  (+) 0과 1사이 무수히 많은 수를 표현 할 수 없어 가장 근접한 값, 즉 근삿값으로 반올림 처리하여 결과를 도출한다.
#  컴퓨터에서 알고리즘을 다루기 위해선 최선의 자료구조를 채택해야 하며,
#  이 자료구조를 구성하는 자료형은 컴퓨터를 기준으로 올바른 사용방법을 알아야만 문제 없이 다음 문제들을 다를 수 있다.
#  결국, 자료형 -> 자료구조 -> 알고리즘 -> 프로그래밍과 같은 관계가 형성 된다.
#
# 6. 알고리즘을 잘하면 무엇을 할 수 있는가?
#  - 네비게이션 경로 문제
#   네비게이션은 특별한 인공지능으로 만들어지지 않았다. 네비게이션 안에는 지도의 경로 데이터와 gps를 통한 현재 내 위치, 그리고 상대가 원하는 위치가
#   입력되어 있다. 이러한 상황에서 gps는 현재 내 위치값을 네비게이션 지도상에 표시하고 이 표시에서 원하는 위치까지의 최단거리나 최소비용 등을
#   검색 알고리즘을 통해서 찾아낸다.
#  - 인터넷 결과 제공 문제
#   수 많은 데이터에서 원하는 정보를 제공하는 것은 초반과는 다르게 점점 데이터의 양이 많아지고 검색의 다양성이 증가하면서 상대가 원하는 정보를
#   찾아주기 위해 알고리즘이 잘 형성되었다. 검색알고리즘 자체 뿐만 아니라 기존에 검색을 했던 것들을 토대로 사람이 원하는 답변이 무엇인지 활용한다.
#   현재는 자료구조 뿐만 아니라 병렬컴퓨팅(문제를 해결하기 위해 다수의 계산 자원을 동시에 사용하는 것)을 이용하여 자료구조 이상의 구조를 통해 속도를 보장해준다.
#  - 신도시 전력, 수도, 상하수 등 인프라 구축 문제
#   도시에서 필수적이고 기반을 만든 후 다시 재공사하기 힘든 부분이 위 문제이다. 즉, 이런 것을 가장 효율적으로 배치해두는 것은 후의 문제를 덜 만들고
#   최적화된 인프라 배치는 최초 공사에 또한 적은 비용으로 넓은 지역을 커버할 수 있도록 함.
#
# 7. 알고리즘을 이해하기 위한 기초 사항
#  - n
#   : 1, 2, 3...과 같이 셀 수 있는 수의 부분을 일반화한 표현. 특정 입력값은 예측하지 못하거나 범위가 광범위하여, 어떤 값이 들어올지 모르는
#   경우가 있다. 이 경우 n이라는 수를 나타내는 기호로써 이를 표현해주기 위해서 사용한다.
#  - 무한대의 개념. limit
#   : '만약 무한대로 늘어난다면...'이라는 의미이다. 1/n이라는 식이 있을 때 n이 무한대로 갈경우 이 식은 0에 수렴한다. 역으로 n이라는 식이 있다면
#   값은 무한대로 발산한다. 식이 아닌 값이 거꾸로의 의미일 수도 있다. n이 0으로 갈경우에는 무한대로 발산할 것이고, n은 0에 수렴하게 된다.
#   무한대라는 개념 자체를 이해하기 난해할 수 있으나 무한대는 고정된 수가 아니다. 그렇다고 수가 여러가지를 가지는 수도 아니다. 수 자체가 무한대,
#   그 자체인 수이다. 그리고 이러한 수에 대해서 다루기 위해 생긴 식이 limit이라는 식이다.
#   이 개념이 알고리즘에서 왜 쓰이는 지는, 효율을 계산할 때 적은 입력은 어느 알고리즘이건 큰 차이가 나지 않다. 이것이 무한대의 개념에 들어와
#   작동했을 때 더 빠른 것이 최종적으로 효율적인 방식이 되기 때문에 내가 만든 알고리즘이 가진 시간을 파악하는 것의 연장선으로서 사용된다.
#   몰라도 크게 지장은 없지만 알면 편한 수학이다.
#  - log(로그)
#   : 로그는 한마디로 정의하면 지수 함수의 역함수이다. 로그 자체를 공부하는 것도 괜찮지만 솔직히 간단하게 몇가지 기본적인 것만 알고 넘어가겠다.
#   log는 밑과 진수 그리고 지수로 나타낸다. log 우측 하단에 작게 써진 것이 밑이며, 간혹 생략되는 경우도 있다. 이 밑은 지수가 달려있는 값이다.
#   진수의 경우의 이 지수가 달려있는 값을 지수로 계산했을 때의 결과이다. 그리고 이 log값의 결과가 지수가 된다. 다음과 같은 관계를 가진다.
#   a^{x} = b <=> log_{a}b = x
#   (이 때, ^는 지수를 표현하기 위한 식으로 {}안의 식이 지수이며, _는 밑을 표현하기 위한 식으로 {}안의 식이 밑이다.)
#   기본적으로 지수 함수는 흔히 2차함수, 3차함수 등을 가리키는 말이고, 이의 역함수인 로그함수는 x가 음수인 경우가 존재하지 않으며, y는 x가 0에
#   가까울수록 음의 무한대로 뻣어나가고, x가 발산할수록 양의 무한대로 뻣어나간다. 지수함수는 y가 0이하가 없는 구조이다. 그리고 이의 역함수이기에
#   로그 함수는 x가 0이하가 없는 것이다. 그리고 여기서 추가적으로 말을 붙인다면 왜 y음수가 없냐고 물어본다면 허수의 개념까지 넘어가기 때문에
#   여기까지 하기로 하자... 대체로 양수만 존재한다고 이해하자.
#  - 함수, f(n)
#   : 입력값 n에 대한 함수를 표현한 식이라는 의미. 함수는 알고리즘마다 다르지만 '그 알고리즘에 n의 입력을 한다'라는 의미로 사용된다.
#  - 시간복잡도
#   : 알고리즘이 입력값에 대한 연산 횟수에 대한 것을 나타내는 것. 대체로 빅-오 표기법을 사용한다.
#  - 시간 측정 방식, O(빅-오)
#   : 알고리즘을 공부하다보면 O(n)이나 O(nlogn)과 같은 식을 만날 수 있다. 이는 시간을 측정하는 방식에 대한 식이다.
#   우리가 검색 알고리즘을 쓸 때, 첫장부터 끝장을 일일이 확인해서 원하는 수를 찾는 알고리즘이라면, 간혹 그 찾는 값이 첫장에 있을 수도, 끝장에서
#   만날 수도 있다. 그럼 이 알고리즘이 걸리는 시간을 표기하는 것을 어떻게 할 것인가? 이를 위해 '최소', '평균', '최대'와 같은 방식으로 알고리즘의
#   시간을 측정한다. 그 중 O표기법은 '아무리 오래 걸려도 이정도 걸린다'를 표현한 표기법이다. 앞선 검색 알고리즘을 대입하면 전자는 1의 횟수,
#   후자는 n의 크기라면 n의 횟수의 연산을 거치는 것을 확인 할 수 있다. 이 경우 빅-오 방식의 표현은 O(n)을 사용한다. 가장 뒷장까지 봐야하는
#   최악의 경우까지 고려한 시간들의 집합을 빅-오 표기법이라 한다.
#  - 최선의 경우와 최악의 경우
#   : 앞선 이러한 식들의 모음을 빅-오 표기법으로 표기를 했다. 그런데 정렬을 할려는 이미 정렬이 완료되어 있다면? 오름차순 정렬을 하려는데 내림차순으로
#   정렬된 식이라면? 정렬 알고리즘마다 다르겠지만 특정 알고리즘은 최선의 경우와 최악의 경우의 수치가 완전히 다르다. 가장 간편한 버블 정렬의 경우
#   정렬이 이미 되어있다면 O(n)의 시간을 가지며, 최악의 경우 O(n^2)의 식을 가진다. 이는 적은 수치에선 큰 차이가 나지 않지만, 100개의 n을 가진
#   경우에는 100이냐, 10000이냐, 즉, 100배 시간차이가 생긴다. 이는 수가 커질수록 더욱 그 경향이 커진다.
#   일부 경우에는 평균적으로 나타내는 경향으로 계산하는 경우도 있는데 대부분 많이 사용하는 퀵정렬은 구현이 쉽고 평균적으로 O(nlogn)의 시간복잡도를
#   가지는 빠른 알고리즘이지만 이미 정렬이 되어 있거나 수치가 한쪽에 쏠린 경우에는, 즉 최악의 경우에는 O(n^2)의 식으로 변하는 식이다.
#   그러나 그런 이미 정렬이 되어 있는 경우가 확률적으로 매우 낮기 때문에 퀵정렬이 많이 사용된다. 때문에 자료구조에 따라 조심해야할 수 있다.
#  - 시간복잡도별 그래프
#   : 교재 24쪽을 보면 이러한 시간복잡도별 그래프가 나타난다. x축은 입력값, y축은 그에 따른 식별 시간복잡도를 나타낸다. 이를 보면 O(n^2)식과
#   O(nlogn)식과의 차이가 선명한 것을 알 수 있다. 우리가 지향해야하는 바가 어떤 것인지 시각적으로 확인할 수 있다.
#
#  8. 재귀(recursion)
#  : 스스로의 식을 해석하기 위해서 스스로를 사용하는 것을 재귀라한다. 그리고 이를 함수로 표현하여 스스로가 스스로를 호출하는 것을 자기호출이라 한다.
#  이러한 자기호출은 컴퓨터 과학 이론의 근간을 이루는 중요한 개념으로, 어떤 문제를 해결하는 과정에서 자신과 똑같지만 크기가 다른 문제를 발견하고
#  이들을 관계로서 문제를 해결하는 접근 방식이다. 이러한 자기호출은 항상 그 끝을 완성하지 않으면 무한의 굴레에 빠지기 때문에 내부에 꼭 굴레를
#  끊어줄 조건이 존재해야한다. 그렇게 보면 조건식이 있기 때문에 재귀가 더 느리지 않을까? 라고 생각할 수 있으나, 컴퓨터 과학에서 모든 처리과정이
#  모두 동등한 연산시간을 가지지 않기 때문에 오히려 효율적임을 알 수 있다.
#  나를 해결하기 위해 나를 부르는 작동은 내부의 알고리즘의 반복되는 부분을 잘 포착했을 때 만들 수 있다. 물론 재귀를 하지 않아도 해결할 수 있으나,
#  재귀를 통하여 훨씬 간단한 표현식이 가능하기에 이를 사용한다. 일부 식은 재귀를 하더라도 속도차이가 없을 수 있으며 재귀를 통해서 속도를 빠르게
#  하려는 것이 아닌 문제해결을 간결화하고 개념적으로 같음을 보장하기 위한 식이라는 점에 집중해야한다.
#
#  9. 수학은 완전무결하며, 모든 수의 답을 낼 수 있는가?
#  : 이 문제는 다음 식을 통해서 알 수 있다. 수학계의 난제중 하나이며, 이를 해결하려한 사람들은 모두 재정신으로 있을 수 없다고 말하는 '콜라츠 추측'
#  이다. 식은 간단한데, 자연수 n에 대하여 홀수 일경우 3n+1을 해주고 짝수일 경우에는 n/2를 해준다. 이 수가 다시 홀수이거나 짝수일 경우 이를 반복한다.
#  이 때, 모든 수는 4, 2, 1에 해당하는 무한 순환에 빠지게 된다는 것이 이 추측의 핵심 내용이다. 이름에서 알 수 있다시피, 이는 '추측'이다.
#  여전히 '방정식', '풀이', '증명'과 같이 해결이 되지 않은 문제다.
#  이 문제에서 알다시피 우리는 이를 증명할 수 없다. 충분한 수(2^68:약 2해를 넘는 수)에서 이 식이 성립됨을 실제 계산으로 입증했으나 모든 자연수에
#  대하여 일반화 되지 않았다. 이 문제는 규칙은 쉬우나 증명하기 어렵다는 모순을 띄고 있어, 쉽게 접근했다가 좌절을 맛보는 경우가 많다.
#  이를 보아도 수학은 현실적인 시간적인 문제를 가질 수도 있다. 현실적인 시간 안에 풀 수라도 있으면 다행이지만 위 문제는 현실적인 시간조차 뛰어넘는
#  수의 무한한 영역에 대한 도전이다. 때문에 이 콜라츠 추측은 증명이 나오기 전까지는 여전히 추측일 것이다. 간단한 규칙 때문에 일련의 수들이 규칙을
#  가질 것이라는 예측과는 다르게 지금까지의 모든 수들을 아무리 다루고 보아도 일반화나 정규화를 할 수 없는 문제이다. 즉, 모든 수를 대입하는 수 밖에
#  이를 증명할 방법이 없다는 것이다.
#  수학의 이러한 모든 것을 해결할 수 없다는 것은 이미 증명되었다. 정지문제라 불리는 엘런 튜링에 의해서 수학이 모든 답에 결론을 낼 수 없다는 진실을
#  논리적으로 규명했다. 이 사고 회로는 아주 간단하다. 모든 식은 해결 가능하다는 것은 곧, 무한 루프에 갇히건 아니건 해결이 가능하다는 것이다.
#  이를 위해 알고리즘이 어떤 특정 입력이 무한 루프에 빠지는지 안빠지는지를 확인해주는 알고리즘이 있다고 가정한다. 구현이 되는지 아닌지는 차치하고서 말이다.
#  이러한 완벽한 알고리즘이 존재한다고 할 때, 이 알고리즘을 이용하여 다음과 같이 새로운 프로그램을 구성한다. 이 프로그램은 루프에 빠지지
#  않으면 무한을 반복하도록 하고, 무한할 경우 무한하다는 것을 알려주고 정지하는 구조로 만든다. 이러한 모든 문제가 해결가능한 프로그램이 있다는 가정을
#  증명하기 위해서 다음을 실행한다. 이 때, 입력은 자기 자신을 받는다. 자기자신을 입력받은 프로그램은 이 프로그램이 무한반복되는지를
#  분석한다. 그럼 프로그램은 둘 중 하나를 낼 것이다. 이 프로그램이 유한하다고 했을 때, 프로그램은 무한 루프에 빠지게 된다. 그럼 프로그램이
#  판단한 자신은 무한루프 때문에 멈추게 된다. 그러나 그렇게 결과를 내면 다시금 자기 자신은 무한루프에 빠지게된다. 모순이다. 분명 이 알고리즘은 모든
#  문제를 해결할 수 있기 때문에 자기자신도 해결할 수 있어야 하지만, 자기자신이 무한대가 되는 문제가 생긴다. 반대의 경우도 같다.
#  무한루프에 빠지지 않는다고 가정한다면 이 분석은 무한이 반복하게 된다. 이 또한 모순이다. 프로그램이 무한루프에 빠지지 않는다고 했는데 빠지는 것이
#  확인 되었기 때문이다. 이를 통해 모든 정답을 해결할 수 있는 것은 존재할 수 없다는 결론이 만들어 진 샘이다. 세상에 이런 완벽한 알고리즘은 존재하지
#  않다. 그리고 이 덕분에, 우리는 여전히 알고리즘을 연구하고 생각해보며 늘 새로운 것을 도전해볼 수 있는 것이다.
#
#  * 수학 이야기
#  - 0 이야기
#   : 태초에 우리는 셀 수 있는 자연수가 존재했습니다. 사과 하나, 포도 다섯송이, 빵 열개 등 자연에서 존재하는 수를 자연수라고 불렀습니다.
#    자연수는 아주 자연스럽게 존재했고 이해하기도 편했습니다. 사과가 5개면 5개이다. 너무나도 쉬운 수였습니다. 그럼 자연수가 존재할 때 0은
#    존재하지 않았을까요? 0은 '없다'라는 개념적으로 존재했습니다. 수로 존재하지않았습니다. 0이라는 수. 즉, 없다라는 수는 자연속에서 있을 수
#    없는 수였습니다. 지금이야 우리가 0이라는 수에 익숙했지만 과거 우리 인류는 그렇지 못했습니다. 한개, 두개처럼 자연적으로 존재하는 것과
#    달리 없음은 개념적인 것이었으니까요.
#    하지만 인간이 손가락으로 수를 세알리기 시작하면서 본격적으로 10진법을 활용하게 되었습니다. 수를 셀 때 가장 가까우면서 누구에게나 동등했던,
#    또, 기계적으로 다룰 수 있는 것이 손가락이었을 테니까요. 물론 이게 10진법이라는 방식이 완벽히 정착했다는 것이 아닙니다. 아직 실질적 10진법은
#    아니었습니다. 다들 비슷한 표기법이었을 뿐이죠. 그렇게 10진법 방식이 등장하면서 문제가 생깁니다. 1에서 9는 자연수로 한자리씩을 표현합니다.
#    그리고 우리는 x라는 하나의 10을 표현하는 10진법을 찾았습니다. 자, 여기서 그럼 다시 11을 표현하려면 다음과 같습니다 x1이건 쉽습니다.
#    값이 점점 증가합니다. 100이라는 수는 어떨까요? x를 10번 써야하나요? 하니면 xx라고 하면 되나요? xx가 편하다고 합시다. 자 그럼 111이 등장합니다.
#    xx는 100이고 x는 10이고 1은... 뭐 1입니다. 이를 더하면 다음과 같습니다. xxx1. 이상합니다. 위 방식대로 늘어나면 결국 xxx는 1000이 될수도 있을
#    텐데 말이죠. 즉, 10진법상 10마다 자리수가 증가해야할 때의 표현에 문제가 생긴 것입니다.
#    자리수가 달라짐을 표현하기 위해서는 격자가 필요하게 됩니다. 즉, xx|x|1을 통해서 111을 표현해야 괜찮은 표현이 된것이죠. 그런데 우리 종이에는
#    항시 격자라는게 없습니다. 그럼 이 숫자가 1001인지 111인지 알 수가 없을 수도 있습니다. 이런 모호한 표현은 문제가 많았습니다.
#    그러던 중 없음을 표현하는 수 0이 등장했을까요? 우선 0보다 먼저 등장한 것이 자리를 채우는 것에 대한 표현이 먼저 등장했습니다.
#    자, 이제 공간을 _로 표현한다고 하겠습니다. 101은 다음과 같이 표현되겠죠. 1_1. 이렇게 되면 이해가 빨라집니다. 1__1은 1001이라는 수겠죠.
#    태초의 0은 이러한 자리수 표현으로 먼저 세상에 나왔습니다. 하지만 여전히 자리수일 뿐, 0이라는 개념자체는 아니었습니다.
#    고대 인도. 0은 드디어 세상에 나오게 됩니다. 없다에 대한 고찰. 어쩌면 철학에 더 가까웠을 이 0이라는 수 표현은 인도의 철학적인 고찰에서
#    나왔습니다. 고대 그리스에서는 0을 수로 표현한다는 것 자체가 어불성설이었습니다. 수란 존재해야했고, 셀 수 있어야합니다. 그런데 0은... 셀수가 없죠.
#    없으니까 말입니다. 그런데 인도에서는 이를 없다는 수로 표현한 것입니다. 태초의 0의 탄생입니다. 물론 이때까지도 개념적 0은 있었지만, 지금과 같이
#    10진법에서의 자리수를 채우면서 없다를 표현하는 0은 정립되지 않았습니다. 정립은 아라비아에서 되었습니다. 흔히 아라비아 숫자라 부르는 수가
#    탄생한 것입니다. 이 때부터 10진법이 본격적으로 사용되었습니다. 이제 우리는 수를 훨씬 쉽게 쓸 수 있게 되었고, 10진법의 정확한 속성을 정의할 수
#    있게 되었습니다. 그리고 이 체계는 10진법 뿐만 아니라 모든 수 체계에서 혁명을 가져왔습니다. 우리가 너무나도 당연하게 쓰고 있는 0.
#    그 수는 없음을 표현하기 위한 철학적인 고민에서부터 시작된 아주 신기한 수입니다.
#
#  - 실수 이야기
#   : 0과 1사이의 수는 몇개일까요? 우리는 이미 0과 1사이에 무한대의 수가 존재한다는 것을 알고 있습니다. 그리고 이 수들의 정체는 자연수가 아닌
#    실수라는 것을 알고 있죠. 우선 태초에 자연수가 있었습니다. 사과 하나. 이런, 배고픈 수학자가 사과를 절반 먹었네요. 여전히 사과는 1개일까요?
#    이 고민에 실수라는 부분이 탄생하게 됩니다. 이미 무엇을 나눈다는 개념은 존재했습니다. 사칙연산은 이미 완성이 되었습니다.
#    2개를 2로 나누면 1개씩 나옵니다. 그럼 1을 2개로 나누면? 앞선 사과와 같이 한개의 사과를 절반을 나누면 수는 더이상 자연수가 아니게 됩니다.
#    이러한 수를 두고 존재하지 않는 수라고 할 수 있을까요? 만약에 그랬다라면 우리는 영영 지구를 벗어나기는 커녕 중세시대를 넘기기도 어려울 것입니다.
#    1을 2로 나눈 수. 1을 3으로 나눈 수와 같이 계산을 하기 위해서는 자연수가 이루는 수의 영역이 존재해야합니다. 사과 하나를 절반으로 만들지 못하면
#    사과 하나로 사람 2명이 나눠먹는 시대는 오지 않았을 것입니다.
#    또한 자연수가 표현할 수 없는 문제가 있었습니다. 바로 연속적인 표현입니다. 쪼개는 방식으로 세상을 이해하면 됩니다. 사과 반쪽을 또 자르면 사과
#    1/4조각이 됩니다. 이를 또 반으로 자르면 1/8, 1/16 하지만 결국 하나의 자연수에서 파생된 것입니다. 연속된 것을 이해하기 위해서는 실수가 필수적입니다.
#    결국 실수는 우리의 삶에 들어왔습니다. 물론 이러한 실수의 정의가 명확히 된 것은 한참 후였지만 말입니다.
#
#  - 피타고라스의 정리 이야기(지구 크기 측정)
#   : 지구의 크기 측정을 최초로 한 시기는 언제일까요? 우주 밖으로 나갔을 때? 대항해시대로 전지구를 항해할 수 있었을 때? 하지만 길이 측정에 대한
#    생각과는 다르게 지구 크기 측정은 이들보다 한참 전인 고대 그리스에서 이뤄졌습니다. 이미 당시 사람들은 각도라는 것을 사용하고 있었습니다. 도형에
#    대한 연구가 활발히 이뤄지고 있었고, 고대 그리스인들은 도형이 가진 속성에서 무언가 규칙을 발견하곤 했습니다.
#    그리고 이 사람. 피타고라스 또한 그랬습니다. 그는 직각삼각형을 들여다보다 이곳에서 규칙을 발견했습니다. 가장 긴 변의 제곱수는 나머지 변의 제곱수의
#    합이라는 사실을 말이죠. 그리고 그 제곱수는 각 변의 길이로 만든 사각형의 넓이라는 것. 그리고 이런 일정 비를 가지는 덕분에 각도에 따른 각 변의
#    비를 계산할 수 있게 되었습니다. 그리고 이것이 바로 sin, cos입니다. 만약에 우리가 고대 그리스 시대 사람이었고 그 발견을
#    처음 들었다면 어땠을까요? 우리는 그 발견에 감탄을 금치 못했을 것입니다. 약간의 직관성이 없다면 그것이 같을 것이라는 생각조차 못할 것입니다.
#    피타고라스의 이런 직관력도 대단하지만 또 다른 사람의 직관력 또한 대단합니다. 에라토스테네스가 바로 그 사람입니다. 이 사람은 최초로 지구의
#    둘레를 계산한, 그러면서 과학적이며, 당시 기술상으로는 거의 정확한 방법으로 측정을 했습니다. 그의 직관력은 무엇일까요? 그는 이집트에 있던 당시
#    우물에 태양빛이 직선으로 꽂히는 것을 보았습니다. 그리고 그 시간은 태양빛에 의해서 생기는 그림자가 가장 작거나 보이지 않을 시간입니다.
#    하지만 다른 지역은 다릅니다. 같은 시간대에 해를 보더라도 직각으로, 그림자가 가장 작은 시기는 존재하지 않습니다. 이미 그 때, 놀랍게도 지구가
#    둥글다는 사실은 어느정도 받아들여지고 있었습니다. 그런것을 보면 딱히 시간이 지날수록 인간이 똑똑해진 건 아닌것 같기도 합니다. 그리고 여기서
#    에라스토테네스는 피타고라스의 정리를 떠올립니다. 지구는 구형, 그리고 그림자의 각도 그리고 각 지역의 거리. 이것만으로 직관적으로 에라스토테네스는
#    지구의 둘레를 잴 수 있다고 생각했습니다. 그의 머리 속에서는 빛은 직각삼각형의 선이고, 그림자는 그에 따라 생기는 각도 차이로 두었습니다.
#    이제 피타고라스의 정리와 sin, cos을 이용하면 각도를 잴 수 있죠. 그리고 실제 지구를 걸으며 지구의 일부분의 거리를 측정하고, 다시 이를
#    지구의 각도에 대입합니다. 뭐 정확한 계산방법은 차지하더라도 이 방식은 그럴듯 했습니다. 다만, 그가 측정할 때 오차가 발생했고 그 때문에
#    지구 둘레크기가 정확히 나오지도 않았으며 전제 자체도 조금 틀렸기 때문에 오차가 발생했지만 당시 기술로는 완벽에 가까운 수준의 크기 비교였습니다.
#    그리고 그 방식 자체에서는 오점을 찾기도 어렵습니다.
#    피타고라스의 정리, sin, cos과 같은 방식은 여전히 활용되고 있습니다. 바로 삼각측량이 그것이죠. 우리에게 3개의 점이 있다면 우리는 앞선 식을
#    사용하여 어떤 거리든, 각도든 측정해낼 수 있습니다.
#
#  - 파이 이야기
#   : 원의 길이를 재는 것은 직각삼각형의 길이를 재는 것과는 매우 어려운 일이었습니다. 둥그런 물체의 길이를 재기 위해서 줄같은 것을 활용할 수
#   있습니다. 그런데 그려진 도형이라면? 이 길이는 어떻게 측정하죠? 또한 다른 도형 크기를 재는 것처럼 원 또한 크기를 찾고 싶었습니다. 하나의
#   완벽한 식을 찾는 것이 너무나도 필요한 것이었습니다. 그럼 원은 어떻게 그려질까요? 우선 기본적으로 원은 하나의 중심점으로 같은 위치의 점들을
#   전부 이은 것입니다. 이 방식을 채용해서 우선 한 점에서 6개의 점만 찍고 선을 그려보겠습니다. 이 때, 6각형이 나옵니다. 정육각형이죠. 우선
#   정육각형의 각 선의 길이가 이 육각형의 둘레가 되겠죠. 하지만 원과 비교했을 때 빈공간이 생깁니다. 이에 대해 원의 공간을 측정하려면 이 공간을
#   줄여가야합니다. 그리고 이를 비교하기 위해서는 내접하는 정육각형이 아닌 원에 외접하는 정육각형을 만들겠습니다. 그리고 이 정육각형과 내접하는
#   정육각형의 사이가 바로 원의 둘레가 되겠죠. 자 그럼 계속 가보겠습니다. 이번엔 정팔각형을 원에 내접 및 외접하게 그려보겠습니다. 점점 두 사이의
#   빈공간이 좁아집니다. 원에 점점 가까운 값을 알아낼 수 있습니다. 이렇게 계속 가다보면 어느 순간 거의 원에 가까운 각형이 만들어집니다.
#   외접도형과 내접도형 간의 크기 차이를 보기 힘든 수준에 오게되면 그것이 바로 원의 둘레가 될 수 있을 것입니다.
#   뭐 대충 3.141592... 정도 비율이 있네요. 하지만 이 끝이 있을 것이라는 확신은 없습니다.
#   그런데 이런식으로 계속 가다보면 문제가 발생합니다. 수의 끝인 존재하는가요?
#
#  - 무한대 이야기
#   : 수는 끝이 없습니다. 아마 우주 끝에서 우주끝까지 수를 나열해놓는다고 해도 그것이 수의 끝은 아닐 것입니다. 우주를 전부 수로 채워볼까요?
#   그래도 수는 끝이 없습니다. 우주가 좀더 많이 필요하겠내요. 우리는 이 셀 수는 있지만 다가갈 수 없는 수에 대한 논쟁을 받습니다. 그것이 수가
#   아닌가? 직관적으로 그런 수는 수가 아니었습니다. 직관주의자들은 무한은 존재할 수 없는 수로 규명했습니다. 하지만 형식주의자들은 달랐습니다.
#   직관적이지 않다고 해서 존재하지 않는 것은 아니었습니다. 그렇게 치면 0도 매한가지니까요. 실수는 또 어떨까요? 결국 사과 1개라고 표현했을 뿐이지,
#   사과 분자 x개? 사과 분자의 원자 y개? 이런 식으로 표현하면 실수 또한 허상에 불가할지 모르죠. 계산을 위해서는 무한대의 개념이 필요했습니다.
#   앞선 파이와 같습니다. 아무리 다각형의 각이 많다고(예를 들어 10000각형과 같은) 해서 그게 원인 것은 아닙니다. 세세하게 들어가면 결국 다각형에
#   불가합니다. 그렇기 때문에 원에 가까워지기 위해서는 원에 가까울 정도로 각을 늘려야합니다. 그렇기 위해서 필요한 수단이 무한대입니다.
#   파이를 계산한 건 고대 그리스 시대입니다. 그러나 그런 그들도 0과 더불어 무한대의 개념을 인정하지 않았습니다. 그저 충분히~ 이정도면 이라는 식으로
#   무한대로 가는 문제를 피했습니다. 결국 무한대는 중세를 넘어서야 본격적으로 이야기되기 시작했습니다.
#   무한대를 이해하기 위해서 가장 자주 쓰이는 것이 힐베르트의 호텔입니다. 이 호텔방은 무한개입니다. 뭐 그게 가능하냐 마냐는 사고 속에서 있는
#   호텔이니 무시하도록 하겠습니다. 괜히 부동산이 어쩌고, 집값이 어쩌고 방을 찾아가려면 어쩌고 하면 이 개념을 이해하지 못합니다. 부동산은 상관없고,
#   집 값은 뭐 무한대로 있다고 하고, 또 방을 찾아가는 시간은 단 1초면 된다고 칩시다. 그게 아무리 먼방이라도 말이죠. 이 무한대의 호텔에 어느날
#   무한대의 사람들이 찾아왔습니다. 방이 모두 찼습니다. 그런데 한손님이 또 들어오네요. 호텔에 방은 없습니다. 그래서 지배인은 그 손님을 받을 수
#   없을까요? 지배인은 머리를 굴렸습니다. 호텔 전체에 마이크를 켰죠. 지배인은 모든 객실의 사람들일 각자 호실의 +1로 이동하라고 지시했습니다.
#   무한대의 사람은 그것을 수용했습니다. 그렇게 이동하고 나니 1호실이 비었군요. 1호실 사람은 2호실로 갔을테니까요. 이제 이 1호실을 이 손님에게
#   주면 됩니다. 뭐 이런 사람들이 있을 수 있습니다. 무한대의 사람을 무한대에 채우면 +1은 존재하지 않는 것 아니냐? 근데 그건 무한대를 잘못 이해한 것이죠.
#   무한대의 방은 무한대입니다. 한계가 없습니다. +1은, 존재할 수 있죠. 그리고 그 개념 자체고 무한대의 개념입니다.
#   자, 그런데 이 호텔에 또다시 무한대의 손님이 찾아왔습니다. 이제 +1방식으로 한번에 방을 할당해 줄 수 없습니다. 지배인은 이번엔 기어코 해고될까요?
#   아닙니다. 지배인은 다시 방송을 켭니다. 모든 객실의 손님은 자신의 방의 x2에 해당하는 호실로 이동하라고 지시했습니다. 그 말을 들은 손님들은
#   뭐 불편이야 하겠지만 어쩌겠습니까. 이동을 합니다. 그럼 이제 1호실 사람은 2호실로 2호실 사람은 4호실로 이동했습니다. 1호실과 3호실, 그리고 그
#   여타의 홀수실이 모두 비었습니다. 이제 이 무한대의 홀수실에 무한대의 사람을 수용합니다. 정말 신기하죠.
#   무한대의 사람을 싣고 무한대의 버스가 도착했습니다. 절체절명의 순간. 지배인은 어떻게 하면 중복이 안될지 고민을 합니다. 단순 2분법은 안되니까요.
#   이 때, 소수의 특성을 사용합니다. 소수는 1과 자기자신으로만 나눌 수 있는 수입니다. 이들을 이용하여 스스로가 스스로를 곱한 값은 절대로 다른
#   수로 나눌 수 없다는 특성이 생기기됩니다. 이러면 됬습니다. 소수는 무한합니다. 각 버스에 각 소수를 배정합니다. 그리고 그 소수에 대하여 각 손님을
#   소수^n을 해줍니다. n은 각 손님의 번호가 되겠죠. 이렇게 방을 배정하면 비는 공간이 뭐 많이 생긴 것 같긴 한데 모든 무한대의 버스의 무한대의 손님을
#   호텔에 받을 수 있게 됬습니다. 뭐 남는 방은 대강 다른 무한대의 손님이 아닌분에게 주죠 뭐.
#   그런데 이런 무한대에도 급이 나눠집니다. 이번에도 무한대의 손님이 찾아왔습니다. 그런데 각 손님은 신기한 이름을 가지고 있습니다. 바로 0과 1사이의
#   실수를 이름으로 가졌습니다. 모두가 말이죠. 그리고 모두가, 중복되는 이름은 없습니다. 이 때, 앞선 방식으로 모두에게 방을 할당했습니다. 하지만
#   이 0과 1사이의 실수의 이름은 다음과 같은 또다른 사실이 있습니다. 0.1과 0.2에 또 다른 무한의 실수가 존재한다는 것입니다. 또 0.11과 0.12사이에도
#   무한개의 실수가 존재합니다. 안타깝게도 자연수 호실인 우리 힐베르트의 호텔에는 그들을 모두 수용할 수 없었습니다. 1과 2사이에 무한대가 존재하지 않는
#   자연수의 무한대와는 차원이 다른 것입니다.
#   무한대는 일부 수식을 이해하는데도 도움을 줍니다. 앞선 limit입니다. x+1일 때 x가 무한대로 향하게 된다면 이 값은 실질적으로 무엇에 가까울 까요?
#   10일 때, 1은 x의 1/10입니다. 꽤 큰 차이를 만듭니다. 그런데 1만이 됩니다. 1은 이제 x의 1/10000입니다. 점점 작아집니다. 이것이 반복됩니다.
#   결국 1은 1/무한대에 도달하게됩니다. 이는 무한대의 수에게서는 딱히 큰 수가 아닙니다. 있어도, 없어도 무한대인건 변함이 없습니다. 마치 호텔의
#   1개의 방을 만들던 문제와 같습니다. 무한대의 개념에서는 가능하죠. 우리는 1/0이 존재할 수 없음을 알고 있습니다. 그런데 1/x가 0에 가까워 진다고
#   0에 무한대로 가까워진다고 가정해보겠습니다. 그렇게 되면 어떻게 될까요? 순수하게 1/0과는 다르게 이 때는 무한대의 수가 됩니다. 불가능한 수식을
#   무한대의 개념으로 계산가능한 수식으로 만든 것입니다.
#
#  - 음수 이야기
#   : 자연수와 실수, 그리고 0이 존재하는 지구에 여전히 없던 수의 세계가 있었습니다. 바로 음수이죠. 수가 없는 것까지는 이해를 했지만, 아니 오히려
#    그 개념은 획기적이고 좋은 개념이었지만 음수는 조금 늦게 받아들여졌습니다. 수가 없음을 넘어선다니? 애초에 그걸 말로 어떻게 표현할 건가요?
#    지금은 마이너스이다, 음수이다라는 좋은 개념이 있었지만 그런 단어조차 없던 시대에 0보다 작은 수가 어떻게 받아들여졌을까요? 아마 음수가 받아들여지기
#    전까지는 대출업하는 사람들은 고생꽤나 했을 것입니다. 오직 양수만 있는 시대에서는 내가 돈을 빌려주면 새로운 개념이 필요했습니다. 빚이라는 개념
#    말입니다. 대출업자 A는 대출자 B에게 1000만원을 빌려줬습니다. B는 +1000만원이되었습니다. 그런데 A는 뭐라고 해야하나요? 1000만원이 있다가
#    없어졌으니 0으로 표현하면 될까요? 하지만 대출업자는 0원이 아닌 돌려받을 수인 1000만원이 필요합니다. 오히려 0에서 1000만원이 된건 B이죠.
#    그렇다고 B에게 늘어난 돈 1000만원은 아무런 패널티가 없는 돈인가요? 그 돈은 갚아야할 돈 입니다. 즉, 이 가상의 돌려 받아야될 돈과 돌려줘야할
#    돈을 표현할 방식이 과거에는 빚이라는 새로운 개념을 만들어야 했고, 상환금 등으로 읽어야했습니다. 음수 개념만 도입해도 이 문제가 깔끔해지는데
#    말입니다.
#    음수는 자연계의 수가 아닙니다. 오히려 개념적인, 철할적인 개념에 더 가깝습니다. 수학을 하는 사람들에게는 음수의 개념이 너무 철학적이라서
#    받아들이기 어려웠습니다. 때문에 음수가 빛을 보기 시작한건 거의 18800년이 넘어셔죠. 실제 계산할 때 사용한다면 음수는 매우 유용합니다.
#    차원을 확장하는데도 상당히 도움이 되죠. 또한 이러한 음수는 0을 기준으로 좌표계를 만들때도 유용했습니다.
#    음수 계산을 쉽게 받아들이지 못하는 건 당연한 처사였습니다. 뭐 합이나 뺄샘은 할 수 있다고 치겠습니다. 그런데 양수 x 음수의 경우에 문제가
#    생깁니다. 애초에 곱셈이라는 개념이 x를 y번 반복 더한다입니다. 그런데 3을 -1번 더한다니? 이게 무슨 소리겠습니까? 천천히 생각하면 이론화
#    시킬 수는 있습니다. 특히 좌표계에 그려보면 쉽습니다. 우선 x는 3으로 고정하겠습니다. y는 다시 특정한 수 x로 바꿉니다. 이 상태에서 각,
#    x의 값에 대한 결과는 y입니다. 음수로 갈필요는 없습니다. 우선 양수 좌표계에서 x가 0부터 10에 대한 자연수에 대한 y의 값을 점으로 찍습니다.
#    그리고 점을 한선으로 그으면 좌표계를 가로지르는 최종적으로 0으로 향하는 하나의 직선이 만들어집니다. 여기에 이제 음수 개념을 도입합니다.
#    음수도 자연수와 같이 늘립니다. 1단위로 말이죠. 이는 근데 자연수는 아닙니다. 우리는 이러한 수 체계를 이제 정수라고 부르기로 했습니다.
#    실수와는 다른 개념입죠. 놀랍게도 음수가 실수보다 늦게 등장한 개념입니다. 자, 우선 결과는 모른다고 생각하겠습니다. 그런데 생각해보면
#    경향이라는 것이 존재합니다. 우리는 딱히 점을 찍을 필요가 없습니다. 양의 좌표계에서 그은 선을 그대로 음의 좌표계로 연결해 이어나가면 됩니다.
#    그리고 이것이 양수와 음수의 곱의 결과입니다. 일부 수학은 오히려 수적인 이해를 위해서 그림을 활용하고는 합니다. 2차방정식과 같은 것들도
#    이를 증명하고 해결하기 위해 시각화하곤 했습니다. 그럼 이제 양수와 음수의 곱이나 나누기는 해결된 셈입니다. 음수와 음수 곱은 어떨까요?
#    다시 양의 좌표계로 이동합니다. y = -3x라는 식이 있습니다. 이미 우리는 3 x -3을 양의 좌표계의 연장으로 증명했습니다. 뭐 곱셈은 위치를
#    바꿔도 똑같습니다. 결국 이 식은 -3 x 3이 될 수도 있고 이는 x는 양의 좌표, y는 음의 좌표계에 해당하는 4사분면의 위치가 됩니다. 이렇게
#    점을 찍고 그런 다음 이선을 또 연장합니다. 그럼 음수 x 음수가 제 2사분면, 즉, y값이 양의 값을 가리키는 것을 확인 할 수 있습니다.
#    이를 통해서 우리는 음수 x 음수가 양수임을 확인할 수 있게 되었습니다.
#    음수는 딱히 엄청난 개념은 아니었습니다. 그러나 수 체계의 근본을 뒤집은 개념임에는 틀림 없습니다.
#
#  - 미적분 이야기
#   : 도량형이라고 아십니까? 도량형이란 물리량을 측정하기 위한 표준 단위를 뜻합니다. 즉, 부피, 둘레, 속도, 무게 등등 각가에서 쓰는 표준 단위,
#    가리키는 단어가 도량형입니다. 이 도량형이 왜 중요하느냐? 과거 왕국단위의 국가를 유지하기위해서는 세금을 걷어야했습니다. 뭐 세금도 결국
#    있는거 다내놔 이런 식으로 할 수는 없는 노릇이었고, 종교적으로 십일조와 같이 일부를 때가는게 익숙할 때였습니다. 돈으로 낼 수도 있었지만
#    대게 농산품 등을 일부를 세금으로 냈습니다. 그러려면 각 농산물에 따라 도량형이 존재해야했습니다. 우리나라로 치면 홉, 말 등 곡식을 세는
#    단위처럼 말이죠. 서양은 그 중 포도주도 세금이었습니다. 포도주의 도량형은 뭐 1잔, 1병, 또는 나무 통에 넣은 1통정도가 되겠죠. 그런데,
#    인간이란게 참 영악한게, 같은 1통이더라도 양을 다르게 넣는 방법을 알아냈다는 것입니다. 포도주 통은 원통모양인데 원통이 조금 튀어나온
#    구조를 가지고 있는데 이 튀어나온 만큼 포도주가 더 들어가는 것은 상식입니다. 어차피 포도주통의 규격을 맞춰야지만 1통이라고 했을 때 어떤 사람은
#    사람만한 통, 어떤 사람은 강아지만한 통이 되지 않을 테니 통의 길이로 기준을 잡았을 것입니다. 길이는 재기 쉬우니까요. 그런데 포도주통처럼
#    좌우가 볼록한 구조는 어떻게 비교해야할까요? 길이 뿐만 아니라 좌우도 재야합니다. 뭐 거기까지 했다고 칩시다. 그럼 통의 두께는 어떻게 하죠?
#    이제 머리가 통째로 아파옵니다. 한번에 좀 계산이 되야 세금 계산도 쉽고 부정부패도 막을 수 있을텐데 그게 쉽지가 않습니다.
#    도량형 통일은 왕국 통제의 기반이기도 했습니다. 말그대로 세금을 위해서도 있었지만 부정부패도 막을 수 있었기 때문에 대부분의 왕국이 국가
#    안정화 목적으로 도량형을 통일하는 일을 했습니다. 단순한 구조라면 계산하기 쉬울테지만 포도주통은 영 계산하기가 어려운 구조였습니다.
#    당최 포도주통 내부의 포도주의 양을 재는 것이 어려웠습니다. 이 때 사용된 것이 바로 적분입니다. 우리가 잴수 있는 부분에 대한 식을
#    적분을 통해서 연속적으로 만들어주는 것입니다. 간단히 다음과 같습니다.
#    정육면체가 있습니다. 이 정윤면체를 자릅니다. 이때 생기는 단면은 넓이입니다. 이 넓이를 마치 종이 쌓듯이 계속 쌓으면 어떨까요? 그러면
#    그 결과는 정육면체의 부피가 된다는 사실을 우리가 알 수 있습니다. 물론 이 경우는 그냥 부피식을 이용하는게 훨씬 빠릅니다. 이제 이 개념을
#    포도주통으로 옮겨갑니다. 이 경우에는 우리가 포도주통의 단면은 재기가 편합니다. 부피는 힘들죠. 이를 단면에 대한 식을 적분해줍니다.
#    이 적분을 통해서 포도주통의 부피를 계산할 수 있게 되었고 우리는 포도주통 별로 부피를 재, 모든 포도주통 속의 액체에 대한 순수한 부피를 계산하여
#    차별없이 모두가 동일한 포도주를 제출하도록 만들었습니다.
#    그에 비해 미분은 조금 늦게 뉴턴에 의해서 발견되었습니다. 뉴턴 말고 다른 사람이 있다고는 하는데 뭐 그건 우리가 알 일은 아니죠. 우선 미분은
#    적분의 반대인 셈입니다. 반대라. 그럼 부피를 넓이로 만드는 식인가요? 네, 맞습니다. 그럼 넓이는 적분하면 무엇이 되나요? 둘레가 됩니다. 계산법상
#    보면 3차함수가 2차함수가 되는 형태가 됩니다. 또 이어서 미분하면 2차함수가 1차함수가 되죠. 이런 관계를 가지고 있습니다.
#    2차 함수의 경우 상승률이 상승하는 모양을 가지기 때문에 일부 가속도(기울기)를 구할 때도 사용됩니다.
#
#  - 허수 이야기
#   : 2의 제곱은 4입니다. 역으로 4의 제곱근은 2이죠. 그런데 말입니다. 2의 제곱근은 무엇일까요? 여기서 등장하는 개념이 유리수와 무리수입니다.
#    정수로 실수를 표현할 수 있다면 유리수입니다. 1/2, 1/3처럼 말입니다. 그에 반해 무리수는 제곱하여 2가 되는 수와 같이 정수로 표현하기 어려운
#    수를 무리수라고 합니다. 그리고 다행히 이러한 수를 표현하기 위해 루트가 존재합니다. 때문에 존재는 하지만 표현이 어려운 수에 대해서도 표현을
#    할 수 있게 되었습니다. 하지만 이런 정수, 실수 사이에서도 허용되지 않는 신기한 수가 존재했습니다. 이를 알기 위해선 다시 음수로 가야합니다.
#    음수를 계산하는 것은 알았습니다. 그런데 제곱수에서 음수의 결과가 음수가 나오는 것은 말이 되지 않습니다. 양수 x 양수 건, 음수 x 음수건 같은
#    수를 곱하게 되면 무조건 양수가 나오게 되어있습니다. 하지만 3차방정식을 풀다보면 음수의 제곱근이 등장합니다. 이런 수는 좌표계에 표기조차 할 수
#    없는 수입니다. 즉, 더이상 시각화조차 할 수 없는 문제가 생긴 것입니다.
#    일부 풀 수 없는 3차 함수들은 결국 해결이 불가능한 문제로 계속해서 남았습니다. 이를 설명하기 위해서는 조금 다른 방법을 채택해야 했습니다.
#    바로 제 3의 축이 있는 복소평면 입니다. 이건 3차원 z축과는 조금 다른 체계입니다. 그리고 이곳에서 새로 만들어진 허수축은 복잡한 수를 표현하기 위해
#    사용됩니다. 이 때, 허수를 이용하여 실수와 함께 표현한 수를 복소수라고 합니다. 즉, 실수와 같이 실제 존재하는 수의 체계와 허수와 같이 추상적인
#    개념의 수, 그리고 실제 수식을 해결하기 위해 이 둘을 함께 사용하는 복소수가 존재하는 것입니다.
#    자연수 - 정수 - 실수 - 복소수의 관계, 허수 - 복소수와 같은 관계가 만들어집니다.
#    허수는 복잡한 수식임에는 사실이지만, 이를 통해서 더 복잡했던 풀이 방식을 간단히 만들었습니다. 그리고 우리가 양자역학, 천체학 등을 풀기위해서는
#    허수라는 추상적인 수 개념을 사용해야합니다. 실존하지 않지만 계산이 되며, 유효한 결과를 만드는 허수는 음수 이상의 비현실적인 수로 받아들여졌습니다.
#    적어도 음수는 개념적으로 가능이라도 했죠. 하지만 허수는 개념부터 수에 맞추기 위해 억지로 만들어진 수와 같았습니다. 수 체계는 현실에서 기반하려고
#    노력했습니다. 자연법칙을 해석하기 위해서는 자연법칙에 위배되는 수가 존재해서는 안되었습니다. 그럼에도 허수는 그 존재만으로 풀 수 없던 난제들을
#    인간이 이해할 수 있도록 해석되었으며 해석 불가능하던 문제들도 풀 수 있었습니다. 결국 허수는 실제로 유용했고 많은 수학문제를 푸는데 사용되었습니다.
#    # 그렇게 자연스럽게 허수가 실제 세상의 수로서 인정받은 것입니다.