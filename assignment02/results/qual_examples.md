# Quality Analysis: Success & Failure Cases

## Example 1

**Query:** 외국인특파협회의 회원을 받아들이기 위해 노력한 협회는?

**Ground Truth Answer:** 일본신문협회

### Results:

- Dense: ❌ MISS
- BM25: ❌ MISS
- Hybrid: ✅ HIT
- Hybrid+Rerank: ✅ HIT

### Top-1 Retrieved (Dense):
```
기자클럽은 태생적으로 배타적이며, 뉴미디어와 외신, 프리랜서 기자의 가입을 제한다고 비판받고 있다. 이에 일본신문협회는 외국인특파협회(外国人特派協会, Foreign Correspondents' Club of Japan) 회원은 일본신문협회 회원과 같은 대우를 받는 정책을 적용하였다. 그리고 1990년대말 로이터가 가부토 클럽(兜倶楽部)에 가입하는 것을 허용...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
기자클럽은 태생적으로 배타적이며, 뉴미디어와 외신, 프리랜서 기자의 가입을 제한다고 비판받고 있다. 이에 일본신문협회는 외국인특파협회(外国人特派協会, Foreign Correspondents' Club of Japan) 회원은 일본신문협회 회원과 같은 대우를 받는 정책을 적용하였다. 그리고 1990년대말 로이터가 가부토 클럽(兜倶楽部)에 가입하는 것을 허용...
```

**✨ Success Case:** Hybrid+Rerank successfully retrieved the answer!
**Reason:** Likely due to better fusion and reranking.

---

## Example 2

**Query:** 한와 라이너가 도입된 해는?

**Ground Truth Answer:** 1986년

### Results:

- Dense: ✅ HIT
- BM25: ❌ MISS
- Hybrid: ❌ MISS
- Hybrid+Rerank: ❌ MISS

### Top-1 Retrieved (Dense):
```
1984년 9월부터 덴노지 역 ~ 히네노 역간에 운전을 개시한 '홈 라이너 이즈미'가 전신이다. 특급 구로시오의 381계 전동차의 히네노 전차구 입선 회송 열차를 좌석 정리권을 필요로 하는 정원제 열차로서 운행해온 것으로 간사이 지방 최초의 홈 라이너였다. 1986년 11월 개정에 따라 운전 구간이 와카야마 역까지 연장되어 한와 라이너로 개칭되어 현재에 이...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
1984년 9월부터 덴노지 역 ~ 히네노 역간에 운전을 개시한 '홈 라이너 이즈미'가 전신이다. 특급 구로시오의 381계 전동차의 히네노 전차구 입선 회송 열차를 좌석 정리권을 필요로 하는 정원제 열차로서 운행해온 것으로 간사이 지방 최초의 홈 라이너였다. 1986년 11월 개정에 따라 운전 구간이 와카야마 역까지 연장되어 한와 라이너로 개칭되어 현재에 이...
```

**⚠️ Failure Case:** All methods failed to retrieve the answer.
**Possible Reasons:** Chunking issue, vocabulary mismatch, or complex query.

---

## Example 3

**Query:** 원자력 심장페이스메이커에서 사용하는 플루토늄 동위 원소는 일반 배터리에 비해 수명이 몇 배 더 긴가?

**Ground Truth Answer:** 5배

### Results:

- Dense: ❌ MISS
- BM25: ❌ MISS
- Hybrid: ❌ MISS
- Hybrid+Rerank: ❌ MISS

### Top-1 Retrieved (Dense):
```
플루토늄-238의 붕괴에서는 거의 해롭지 않은 알파 입자를 방사하고, 감마선 조사를 동반하지 않는다. 그러므로, 이 동위 원소는(~160 mg) 원자력 심장페이스메이커의 에너지원에 사용된다. 원자력 심장페이스메이커에서의 에너지는 일반 배터리보다 5배 더 길다....
```

### Top-1 Retrieved (Hybrid+Rerank):
```
플루토늄-238의 붕괴에서는 거의 해롭지 않은 알파 입자를 방사하고, 감마선 조사를 동반하지 않는다. 그러므로, 이 동위 원소는(~160 mg) 원자력 심장페이스메이커의 에너지원에 사용된다. 원자력 심장페이스메이커에서의 에너지는 일반 배터리보다 5배 더 길다....
```

**⚠️ Failure Case:** All methods failed to retrieve the answer.
**Possible Reasons:** Chunking issue, vocabulary mismatch, or complex query.

---

## Example 4

**Query:** 캘리포늄의 동위 원소 중 질량수가 제일 작은 것의 질량수는 몇인가?

**Ground Truth Answer:** 237

### Results:

- Dense: ✅ HIT
- BM25: ✅ HIT
- Hybrid: ✅ HIT
- Hybrid+Rerank: ✅ HIT

### Top-1 Retrieved (Dense):
```
질량수가 237부터 256까지인 캘리포늄 동위 원소는 핵 반응기에서 만들어진다. 캘리포늄-253은 β-방사를 하는 동위 원소이고 나머지는 α-방사를 하는 동위 원소이다. 질량수가 짝수인 동위 원소 (Cf, Cf and Cf)는 자발 핵분열을 할 확률이 높다. 특히 Cf는 자발 핵분열할 확률이 99.7%이다. 캘리포늄-249는 그나마 긴 반감기 (352년)을...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
질량수가 237부터 256까지인 캘리포늄 동위 원소는 핵 반응기에서 만들어진다. 캘리포늄-253은 β-방사를 하는 동위 원소이고 나머지는 α-방사를 하는 동위 원소이다. 질량수가 짝수인 동위 원소 (Cf, Cf and Cf)는 자발 핵분열을 할 확률이 높다. 특히 Cf는 자발 핵분열할 확률이 99.7%이다. 캘리포늄-249는 그나마 긴 반감기 (352년)을...
```

---

## Example 5

**Query:** 개를 통해 추측한, 인체 1kg당 플루토늄의 치사량은?

**Ground Truth Answer:** 0.32mg

### Results:

- Dense: ✅ HIT
- BM25: ✅ HIT
- Hybrid: ✅ HIT
- Hybrid+Rerank: ✅ HIT

### Top-1 Retrieved (Dense):
```
음식이나 피(예: 상처 등)또는 공기를 통하여 인체에 들어오는 플루토늄은, 주로 폐, 간 그리고 뼈에 축적된다. 그래서 다른 인체 기관에는 단지 10%만 축적된다. 플루토늄은 인체에 10년 이상 잔류한다. 체내에서의 플루토늄의 축적 시간이 긴 이유는 완전히 밝혀지지 않았지만, 플루토늄의 가용성이 매우 약해서 축적 시간이 긴 것으로 추측되고 있다. 플루토늄의...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
음식이나 피(예: 상처 등)또는 공기를 통하여 인체에 들어오는 플루토늄은, 주로 폐, 간 그리고 뼈에 축적된다. 그래서 다른 인체 기관에는 단지 10%만 축적된다. 플루토늄은 인체에 10년 이상 잔류한다. 체내에서의 플루토늄의 축적 시간이 긴 이유는 완전히 밝혀지지 않았지만, 플루토늄의 가용성이 매우 약해서 축적 시간이 긴 것으로 추측되고 있다. 플루토늄의...
```

---

## Example 6

**Query:** 서대구화물역은 어떤 방식으로 공사가 추진되었습니까?

**Ground Truth Answer:** 제3섹터

### Results:

- Dense: ✅ HIT
- BM25: ❌ MISS
- Hybrid: ✅ HIT
- Hybrid+Rerank: ✅ HIT

### Top-1 Retrieved (Dense):
```
1991년 6월에 법인이 설립되고 1993년 9월에 도시계획 시설로 결정되어, 1996년 12월부터 대구광역시와 철도청(당시), 민간업체 22개사가 공동으로 출자하여 ‘제3섹터’ 방식으로 대구광역시 서구 이현동의 부지에 서대구 복합 화물역사를 건립하는 공사가 추진되어 왔으며, 1997년 2월 21일에 대구복합화물터미널 기공식이 열렸다. 하지만 같은 해 12...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
1991년 6월에 법인이 설립되고 1993년 9월에 도시계획 시설로 결정되어, 1996년 12월부터 대구광역시와 철도청(당시), 민간업체 22개사가 공동으로 출자하여 ‘제3섹터’ 방식으로 대구광역시 서구 이현동의 부지에 서대구 복합 화물역사를 건립하는 공사가 추진되어 왔으며, 1997년 2월 21일에 대구복합화물터미널 기공식이 열렸다. 하지만 같은 해 12...
```

---

## Example 7

**Query:** 순수한 악티늄이 만들어진 연도는?

**Ground Truth Answer:** 1950년

### Results:

- Dense: ✅ HIT
- BM25: ❌ MISS
- Hybrid: ✅ HIT
- Hybrid+Rerank: ✅ HIT

### Top-1 Retrieved (Dense):
```
악티늄은 1899년에 마리 퀴리의 도움으로 드비에른에 의해 발견되었다. 라듐과 폴로늄을 빼고 남은 피치블렌드 찌꺼기에서 발견된 것이다. 1899년 당시, 그는 이 물질이 티타늄과 비슷했다고 하였다. 또, 1900년 당시에는 토륨과도 비슷했다고 했다. 1971년에 악티늄의 발견자가 드비에른이 맞는 지에 대한 논쟁이 일어나기도 하였다. 그리고 2000년에도 일...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
악티늄은 1899년에 마리 퀴리의 도움으로 드비에른에 의해 발견되었다. 라듐과 폴로늄을 빼고 남은 피치블렌드 찌꺼기에서 발견된 것이다. 1899년 당시, 그는 이 물질이 티타늄과 비슷했다고 하였다. 또, 1900년 당시에는 토륨과도 비슷했다고 했다. 1971년에 악티늄의 발견자가 드비에른이 맞는 지에 대한 논쟁이 일어나기도 하였다. 그리고 2000년에도 일...
```

---

## Example 8

**Query:** 히네노 역 이남 지역에서 우선도가 높은 열차는?

**Ground Truth Answer:** 특급

### Results:

- Dense: ❌ MISS
- BM25: ❌ MISS
- Hybrid: ❌ MISS
- Hybrid+Rerank: ❌ MISS

### Top-1 Retrieved (Dense):
```
대낮 시간대에는 덴노지 역 ~ 히네노 역 간에서 쾌속과 보통이 각각 시간당 6편씩 운전되고 있다. 히네노 역 이남 구간 (~와카야마 역)의 운전 편수는 오사카 방면에서 온 대부분의 열차가 히네노 역에서 종착하기 때문에 히네노 역 이북 구간의 열차 편수에 비해 비교적 적은 편이다. 또 히네노 역 이남 지역의 특급의 우선도가 높기 때문에 히네노 역·이즈미스나가...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
대낮 시간대에는 덴노지 역 ~ 히네노 역 간에서 쾌속과 보통이 각각 시간당 6편씩 운전되고 있다. 히네노 역 이남 구간 (~와카야마 역)의 운전 편수는 오사카 방면에서 온 대부분의 열차가 히네노 역에서 종착하기 때문에 히네노 역 이북 구간의 열차 편수에 비해 비교적 적은 편이다. 또 히네노 역 이남 지역의 특급의 우선도가 높기 때문에 히네노 역·이즈미스나가...
```

**⚠️ Failure Case:** All methods failed to retrieve the answer.
**Possible Reasons:** Chunking issue, vocabulary mismatch, or complex query.

---

## Example 9

**Query:** 프로 배구 출범 이래 처음으로 해외에 진출한 여자 배구 선수는 누구인가?

**Ground Truth Answer:** 김연경

### Results:

- Dense: ✅ HIT
- BM25: ✅ HIT
- Hybrid: ❌ MISS
- Hybrid+Rerank: ❌ MISS

### Top-1 Retrieved (Dense):
```
자국 리그에서 "최고의 공격수"로 불리며 활약하는 동안, 이를 지켜보는 많은 팬들과 관계자들은 김연경을 해외에 진출시키는 것이 한국 배구를 위한 길이라고 주장하였다. 또한 김연경 자신도 해외 진출을 희망하고 있으며, 소속 팀 흥국생명은 김연경이 더 넓은 무대에서 활동할 수 있도록 2008~2009 시즌 이후 임대 형식으로 해외 리그 진출을 모색하겠다는 의사...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
자국 리그에서 "최고의 공격수"로 불리며 활약하는 동안, 이를 지켜보는 많은 팬들과 관계자들은 김연경을 해외에 진출시키는 것이 한국 배구를 위한 길이라고 주장하였다. 또한 김연경 자신도 해외 진출을 희망하고 있으며, 소속 팀 흥국생명은 김연경이 더 넓은 무대에서 활동할 수 있도록 2008~2009 시즌 이후 임대 형식으로 해외 리그 진출을 모색하겠다는 의사...
```

**⚠️ Failure Case:** All methods failed to retrieve the answer.
**Possible Reasons:** Chunking issue, vocabulary mismatch, or complex query.

---

## Example 10

**Query:** 잊혀져 있는 파우스트 서곡 1악장을 부활시킨 것은 누구인가?

**Ground Truth Answer:** 리스트

### Results:

- Dense: ✅ HIT
- BM25: ❌ MISS
- Hybrid: ❌ MISS
- Hybrid+Rerank: ❌ MISS

### Top-1 Retrieved (Dense):
```
한편 1840년부터 바그너와 알고 지내던 리스트가 잊혀져 있던 1악장을 부활시켜 1852년에 바이마르에서 연주했다. 이것을 계기로 바그너도 이 작품에 다시 관심을 갖게 되었고, 그 해 9월에는 총보의 반환을 요구하여 이를 서곡으로 간추린 다음 수정을 했고 브라이트코프흐 & 헤르텔 출판사에서 출판할 개정판도 준비했다. 1853년 5월에는 리스트가 이 작품이 ...
```

### Top-1 Retrieved (Hybrid+Rerank):
```
한편 1840년부터 바그너와 알고 지내던 리스트가 잊혀져 있던 1악장을 부활시켜 1852년에 바이마르에서 연주했다. 이것을 계기로 바그너도 이 작품에 다시 관심을 갖게 되었고, 그 해 9월에는 총보의 반환을 요구하여 이를 서곡으로 간추린 다음 수정을 했고 브라이트코프흐 & 헤르텔 출판사에서 출판할 개정판도 준비했다. 1853년 5월에는 리스트가 이 작품이 ...
```

**⚠️ Failure Case:** All methods failed to retrieve the answer.
**Possible Reasons:** Chunking issue, vocabulary mismatch, or complex query.

---

