![[Pasted image 20230406090856.png]]
![[Pasted image 20230406091012.png]]
![[Pasted image 20230406105636.png]]
![[Pasted image 20230406161126.png]]
## cli
### demangling
输出main.cpp.o中的所有外部链接，并将名字还原
`nm ./main.cpp.o |c++filt -t`