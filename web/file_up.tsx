	const { id: shopId } = useParams<{ id: string }>();
	// RTK - 랩핑샵 댓글작성(POST)
	const [onShopCommentPostRTK, queryInfo] = RTK.usePostWrappingCommentMutation();
	console.log(queryInfo);

	const [review, setReview] = useState<string>("");
	const onChangeShopComment = (e: ChangeEvent<HTMLTextAreaElement>): void => {
		setReview(e.target.value);
	};

	// 별을 클릭했을 때 별점을 업데이트하는 함수
	const [star, setStar] = useState<number>(0);
	const handleStarClick = (starNumber: number) => {
		setStar(starNumber);
	};

	// 재방문 의사 함수
	const [revisit, setRevisit] = useState<boolean>(false);
	const handleRevisitChange = (value: boolean) => {
		console.log(value);
		setRevisit(value);
	};
	const [fileInfo, setFileInfo] = useState<File[]>([]);
	const onActionImgResize = async (files: File): Promise<File | undefined> => {
		const options = {
			maxSizeMB: 1, // 1000000b === 1000kb === 1mb //
			maxWidthOrHeight: 3000,
			useWebWorker: true,
		};
		try {
			const compressBlob = await imageCompression(files, options);
			const compressFile = new File([compressBlob], files.name, {
				type: files.type,
			});
			console.log("리사이징 완료");
			return compressFile;
		} catch (error) {
			console.log(error);
		}
	};

	const [previewImages, setPreviewImages] = useState<string[]>([]);

	const onChangeShopFiles = async (e: ChangeEvent<HTMLInputElement>): Promise<void> => {
		if (e.target.files) {
			const files = e.target.files;
			const totalImages = previewImages.length + files.length;

			if (totalImages > 4) {
				alert("최대 4장의 이미지만 업로드할 수 있습니다.");
				return;
			}

			const compressFiles: File[] = [...fileInfo];
			const previewFiles: string[] = [...previewImages];

			const readImageFile = (file: File): Promise<string> => {
				return new Promise((resolve, reject) => {
					const reader = new FileReader();
					reader.onloadend = () => {
						const src = reader.result as string;
						resolve(src);
					};
					reader.onerror = reject;
					reader.readAsDataURL(file);
				});
			};

			for (let i = 0; i < files.length; i++) {
				const file = files[i];
				const compressImg = await onActionImgResize(file);
				if (compressImg instanceof File) {
					compressFiles.push(compressImg);
					const src = await readImageFile(compressImg);
					previewFiles.push(src);
				}
			}

			setPreviewImages(previewFiles);
			setFileInfo(compressFiles);
		}
	};

	const onSubmitShopComment = (e: FormEvent<HTMLFormElement>): void => {
		e.preventDefault();
		const formData = new FormData();
		formData.append("data", new Blob([JSON.stringify({ review, star, revisit })], { type: "application/json" }));
		fileInfo.forEach((file) => {
			formData.append("images", file);
		});
		console.log(formData);
		onShopCommentPostRTK({ shopId, formData });
		setFileInfo([]);
		setPreviewImages([]);
		setReview("");
		setRevisit(false);
		setStar(0);
	};

	const [clicked, setClicked] = useState<boolean | null>(null);
	const { nickname } = RTK.useAppSelector(RTK.selectDecode);
	const handleRevisitClick = (value: boolean) => (e: React.MouseEvent<HTMLButtonElement>) => {
		e.preventDefault();
		handleRevisitChange(value);
		setClicked(value);
	};

	const fileInputRef = React.useRef<HTMLInputElement>(null);

	const handleFileClick = (e: React.MouseEvent<HTMLButtonElement>) => {
		e.preventDefault();
		fileInputRef.current && fileInputRef.current.click();
	};

<SC.ReviewFormLayout $jc='space-between' $fd='column' $ai='normal' $gap={10} onSubmit={onSubmitShopComment}>
				<SC.FlexBox $jc='space-between'>
					<SC.ReviewUserButtonInner $jc='space-between' $gap={20}>
						<SC.ReviewFromUserName $jc='flex-start' $ai='flex-start'>
							{nickname}
						</SC.ReviewFromUserName>
						<CP.ReviewStarPointer
							star={star}
							width={`20px`}
							height={`20px`}
							handleStarClick={handleStarClick}
						/>
						<SC.FlexBox $gap={10}>
							<CP.DetailButton.PositiveButton
								$buttonSize='revisit'
								value='true'
								onClick={handleRevisitClick(true)}
								$clicked={clicked === true}>
								{"재방문 의사"}
							</CP.DetailButton.PositiveButton>
							<CP.DetailButton.NegativeButton
								$buttonSize='never'
								value='false'
								onClick={handleRevisitClick(false)}
								$clicked={clicked === false}>
								{"재방문 없음"}
							</CP.DetailButton.NegativeButton>
						</SC.FlexBox>
					</SC.ReviewUserButtonInner>
					<CP.DetailButton.SubmitButton $buttonSize='submit' type='submit' children={"리뷰 작성하기"} />
				</SC.FlexBox>
				<SC.ReviewFormInputInner>
					<SC.ReviewFormInput
						value={review}
						name='review'
						onChange={onChangeShopComment}
						placeholder='댓글입력해주세요'
					/>
				</SC.ReviewFormInputInner>
				<SC.FlexBox $jc='flex-start' $gap={previewImages.length > 0 ? 10 : 0}>
					<SC.ReviewPreviewImageInner $gap={10}>
						{previewImages.map((src: string, index: number) => (
							<SC.ReviewPreviewImageItem key={index} src={src}></SC.ReviewPreviewImageItem>
						))}
					</SC.ReviewPreviewImageInner>
					<SC.FlexBox $ai='flex-start'>
						<CP.DetailButton.UploadButton $buttonSize='upload' onClick={handleFileClick}>
							사진업로드+
						</CP.DetailButton.UploadButton>
						<input

							ref={fileInputRef}
							style={{ display: "none" }}
							type='file'
							name='image'
							accept='.png, .jpg, .jpeg'
							onChange={onChangeShopFiles}
							multiple	/>
					</SC.FlexBox>
				</SC.FlexBox>
			</SC.ReviewFormLayout>

*/
